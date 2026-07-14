"""
============================================================
agents/decision_agent.py
============================================================

DecisionAgent
-------------
Combines strategy signals, AI review, risk assessment, and market
regime (plus optional options analysis, dynamic risk, and portfolio
valuation) into one final, explainable trading decision.

Design goals (per review priority #1):

    - Deterministic core: identical inputs always produce an
      identical decision. No hidden randomness, no LLM call inside
      this class -- that belongs to AITradingAgent. This class only
      *merges* what other agents already produced.

    - Explainable: every decision carries a `reasoning` list (plain
      English strings) showing exactly which factors pushed it
      toward BUY / SELL / HOLD, and a `score_breakdown` dict with
      the numeric contribution of each input dimension. Nothing is
      a black box -- you can log `reasoning` straight to your trade
      journal.

    - Veto-based safety: certain risk statuses or AI recommendations
      force HOLD unconditionally, before any scoring happens. Vetoes
      always win over the weighted score -- this is a circuit
      breaker layer, not something confidence can talk its way past.

    - Confidence is a single 0-100 score from a transparent weighted
      blend of strategy/AI/risk/regime, not the strategy's raw
      confidence passed straight through.

IMPORTANT -- assumptions that need verification against your real
agents (this class was written without seeing RiskAgent's or
AITradingAgent's actual source, only the shapes referenced elsewhere
in the reviewed TradingEngine):

    - `risk["status"]` is assumed to be one of:
      LOW / OK / NORMAL / MODERATE / ELEVATED / HIGH / CRITICAL / BLOCKED
      (case-insensitive). Adjust STATUS_SCORES / RISK_VETO_STATUSES
      below if your RiskAgent uses different labels.

    - `ai_review["recommendation"]` is assumed to be one of:
      BUY / APPROVE / SELL / NEUTRAL / REJECT / BLOCK / DO_NOT_TRADE
      (case-insensitive), with `ai_review["confidence"]` 0-100.
      Adjust AI_VETO_RECOMMENDATIONS / the direction map below if
      your AITradingAgent's output schema differs.

    - `regime["regime"]` is assumed to be one of:
      BULL / TRENDING_UP / BEAR / TRENDING_DOWN / RANGE / SIDEWAYS /
      CHOPPY / HIGH_VOLATILITY. Adjust the favorable-direction map
      below to match MarketRegimeDetector's actual regime labels.

    - `options["viable"]` (bool) and `options["implied_volatility"]`
      (float) are read defensively (only applied if present) so this
      works whether or not OptionsAnalyzer produces those fields.

    - `valuation` is currently accepted and threaded through for
      audit/context purposes (see `context` in the result) but not
      yet used quantitatively in scoring -- see TODO in `analyze()`.
      Once you confirm what exposure/concentration fields
      PortfolioValuation actually produces, this is the natural
      place to add an exposure-based score component.
============================================================
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DecisionWeights:
    """
    Weights are configurable rather than hardcoded inline, so tuning
    the decision engine doesn't require touching the scoring logic
    itself. Defaults reflect a conservative, AI-and-risk-gated
    model: risk and AI matter almost as much as the raw strategy
    signal, regime is a smaller tiebreaker/context factor.
    """
    strategy: float = 0.35
    ai: float = 0.30
    risk: float = 0.20
    regime: float = 0.15

    def normalized(self) -> "DecisionWeights":
        total = self.strategy + self.ai + self.risk + self.regime
        if total <= 0:
            raise ValueError("DecisionWeights must sum to a positive number")
        return DecisionWeights(
            strategy=self.strategy / total,
            ai=self.ai / total,
            risk=self.risk / total,
            regime=self.regime / total,
        )


class DecisionAgent:
    """
    Merges strategy, risk, AI review, and market regime (plus
    optional options analysis, dynamic risk, and portfolio
    valuation) into one explainable trading decision.
    """

    # Risk statuses that immediately veto any trade regardless of
    # score. VERIFY against RiskAgent's actual status vocabulary.
    RISK_VETO_STATUSES = {"CRITICAL", "BLOCKED", "BREACHED"}

    # AI recommendations that immediately veto a trade. VERIFY
    # against AITradingAgent's actual recommendation vocabulary.
    AI_VETO_RECOMMENDATIONS = {"REJECT", "BLOCK", "DO_NOT_TRADE"}

    # Risk status -> 0-100 score. VERIFY against RiskAgent.
    STATUS_SCORES = {
        "LOW": 90.0,
        "OK": 90.0,
        "NORMAL": 85.0,
        "MODERATE": 60.0,
        "ELEVATED": 45.0,
        "HIGH": 25.0,
        "CRITICAL": 0.0,
        "BLOCKED": 0.0,
    }

    # Regime -> which direction it favors (+1 bullish, -1 bearish,
    # 0 neutral/no edge). VERIFY against MarketRegimeDetector.
    REGIME_DIRECTION = {
        "BULL": 1,
        "TRENDING_UP": 1,
        "BEAR": -1,
        "TRENDING_DOWN": -1,
        "RANGE": 0,
        "SIDEWAYS": 0,
        "CHOPPY": 0,
        "HIGH_VOLATILITY": 0,
    }

    def __init__(
        self,
        weights: Optional[DecisionWeights] = None,
        buy_threshold: float = 62.0,
        sell_threshold: float = 38.0,
    ):
        """
        buy_threshold / sell_threshold operate on the 0-100 combined
        score. A score strictly above buy_threshold with a bullish
        underlying direction becomes BUY; strictly above
        buy_threshold with a bearish direction becomes SELL; a score
        strictly below sell_threshold becomes HOLD. Between the two
        thresholds is a deliberate dead zone that also resolves to
        HOLD -- this avoids flip-flopping on marginal scores near a
        single cutoff.
        """
        if buy_threshold <= sell_threshold:
            raise ValueError("buy_threshold must be greater than sell_threshold")

        self.weights = (weights or DecisionWeights()).normalized()
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    # -----------------------------------------------------------
    # Public API
    # -----------------------------------------------------------

    def analyze(
        self,
        portfolio: Dict[str, Any],
        market: Dict[str, Any],
        strategy: Dict[str, Any],
        risk: Dict[str, Any],
        ai_review: Dict[str, Any],
        regime: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None,
        dynamic_risk: Optional[Dict[str, Any]] = None,
        valuation: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Produce a final trading decision.

        Returns a dict with:
            action:          "BUY" | "SELL" | "HOLD"
            confidence:      float 0-100
            strategy:        str (strategy name)
            regime:          str (regime name)
            reasoning:        List[str] -- human-readable decision trail
            score_breakdown: Dict[str, float] -- numeric contribution
                             of each input dimension
            vetoed:          bool -- True if a hard veto short-circuited
                             scoring entirely
            context:         Dict[str, Any] -- raw inputs echoed back
                             for downstream audit/logging (currently
                             includes valuation; not used in scoring
                             yet, see module docstring TODO)
        """

        reasoning: List[str] = []

        # ---------------------------------------------------
        # 1. Hard vetoes always win -- no scoring needed.
        # ---------------------------------------------------
        veto_source = self._check_vetoes(risk, ai_review, reasoning)
        if veto_source is not None:
            return self._build_result(
                action="HOLD",
                confidence=0.0,
                strategy=strategy,
                regime=regime,
                reasoning=reasoning,
                score_breakdown={"veto_source": veto_source},
                vetoed=True,
                valuation=valuation,
            )

        # ---------------------------------------------------
        # 2. Score each input dimension 0-100, and get each
        #    dimension's directional lean (+1 bullish, -1 bearish,
        #    0 neutral) where applicable.
        # ---------------------------------------------------
        strategy_score, strategy_direction = self._score_strategy(strategy, reasoning)
        ai_score, ai_direction = self._score_ai(ai_review, reasoning)
        risk_score = self._score_risk(risk, dynamic_risk, reasoning)
        regime_score, regime_direction = self._score_regime(
            regime, strategy_direction, reasoning
        )

        # ---------------------------------------------------
        # 3. If strategy/AI/regime actively disagree on direction,
        #    that disagreement is itself a risk signal -- apply a
        #    flat penalty rather than let the weighted average paper
        #    over a real conflict.
        # ---------------------------------------------------
        directions = [d for d in (strategy_direction, ai_direction, regime_direction) if d != 0]
        agreement_penalty = 0.0
        if directions and any(d != directions[0] for d in directions):
            agreement_penalty = 20.0
            reasoning.append(
                "Strategy/AI/regime directional disagreement detected -- "
                f"applying a {agreement_penalty:.0f}-point confidence penalty."
            )

        combined_score = (
            self.weights.strategy * strategy_score
            + self.weights.ai * ai_score
            + self.weights.risk * risk_score
            + self.weights.regime * regime_score
        )
        combined_score = max(0.0, combined_score - agreement_penalty)

        # ---------------------------------------------------
        # 4. Options viability/IV, if provided, can only pull the
        #    score down -- it's a sanity check, never a reason to
        #    trade on its own.
        # ---------------------------------------------------
        combined_score = self._apply_options_penalty(combined_score, options, reasoning)

        # TODO: portfolio `valuation` (exposure, concentration, cash
        # available) isn't scored yet -- once the real field names
        # from PortfolioValuation/PortfolioAllocator are confirmed,
        # add an exposure-based score component here (e.g. penalize
        # combined_score if this trade would push sector/position
        # concentration past a configured limit). Currently only
        # echoed back in `context` for audit purposes.

        # ---------------------------------------------------
        # 5. Map combined score + direction to a final action using
        #    the buy/sell thresholds with a dead zone between them.
        # ---------------------------------------------------
        overall_direction = strategy_direction if strategy_direction != 0 else ai_direction

        if combined_score > self.buy_threshold and overall_direction > 0:
            action = "BUY"
        elif combined_score > self.buy_threshold and overall_direction < 0:
            action = "SELL"
        elif combined_score < self.sell_threshold:
            action = "HOLD"
            reasoning.append(
                f"Combined score {combined_score:.1f} below hold threshold "
                f"{self.sell_threshold:.1f} -- staying flat."
            )
        else:
            action = "HOLD"
            reasoning.append(
                f"Combined score {combined_score:.1f} in dead zone "
                f"({self.sell_threshold:.1f}-{self.buy_threshold:.1f}) -- holding rather "
                "than acting on a marginal signal."
            )

        reasoning.append(f"Final combined score: {combined_score:.1f}/100 -> action={action}")

        return self._build_result(
            action=action,
            confidence=round(combined_score, 2),
            strategy=strategy,
            regime=regime,
            reasoning=reasoning,
            score_breakdown={
                "strategy_score": round(strategy_score, 2),
                "ai_score": round(ai_score, 2),
                "risk_score": round(risk_score, 2),
                "regime_score": round(regime_score, 2),
                "agreement_penalty": agreement_penalty,
                "combined_score": round(combined_score, 2),
            },
            vetoed=False,
            valuation=valuation,
        )

    # -----------------------------------------------------------
    # Internal scoring helpers
    # -----------------------------------------------------------

    def _check_vetoes(
        self, risk: Dict[str, Any], ai_review: Dict[str, Any], reasoning: List[str]
    ) -> Optional[str]:
        risk_status = str(risk.get("status", "")).upper() if isinstance(risk, dict) else ""
        if risk_status in self.RISK_VETO_STATUSES:
            reasoning.append(f"VETO: risk status '{risk_status}' forces HOLD.")
            return "risk"

        ai_recommendation = (
            str(ai_review.get("recommendation", "")).upper()
            if isinstance(ai_review, dict) else ""
        )
        if ai_recommendation in self.AI_VETO_RECOMMENDATIONS:
            reasoning.append(f"VETO: AI recommendation '{ai_recommendation}' forces HOLD.")
            return "ai"

        return None

    def _score_strategy(self, strategy: Dict[str, Any], reasoning: List[str]):
        if not isinstance(strategy, dict):
            reasoning.append("Strategy payload missing/invalid -- scoring as neutral (0).")
            return 0.0, 0

        signal = str(strategy.get("signal", "HOLD")).upper()
        confidence = self._to_float(strategy.get("confidence", 0))
        direction = {"BUY": 1, "SELL": -1, "HOLD": 0}.get(signal, 0)

        reasoning.append(
            f"Strategy '{strategy.get('strategy', 'UNKNOWN')}' signals {signal} "
            f"at {confidence:.1f} confidence."
        )

        return confidence, direction

    def _score_ai(self, ai_review: Dict[str, Any], reasoning: List[str]):
        if not isinstance(ai_review, dict):
            reasoning.append("AI review payload missing/invalid -- scoring as neutral (50).")
            return 50.0, 0

        recommendation = str(ai_review.get("recommendation", "NEUTRAL")).upper()
        confidence = self._to_float(ai_review.get("confidence", 50))
        direction = {"BUY": 1, "APPROVE": 1, "SELL": -1, "NEUTRAL": 0}.get(recommendation, 0)

        reasoning.append(
            f"AI review recommends '{recommendation}' at {confidence:.1f} confidence."
        )

        return confidence, direction

    def _score_risk(
        self,
        risk: Dict[str, Any],
        dynamic_risk: Optional[Dict[str, Any]],
        reasoning: List[str],
    ) -> float:
        if not isinstance(risk, dict):
            reasoning.append("Risk payload missing/invalid -- scoring conservatively (30).")
            return 30.0

        status = str(risk.get("status", "UNKNOWN")).upper()
        score = self.STATUS_SCORES.get(status, 50.0)
        reasoning.append(f"Risk status '{status}' -> risk score {score:.1f}.")

        if isinstance(dynamic_risk, dict):
            dyn_status = str(dynamic_risk.get("status", "")).upper()
            if dyn_status in self.STATUS_SCORES:
                dyn_score = self.STATUS_SCORES[dyn_status]
                reasoning.append(
                    f"Dynamic risk status '{dyn_status}' -> {dyn_score:.1f}; "
                    "blended with static risk score."
                )
                score = (score + dyn_score) / 2

        return score

    def _score_regime(
        self, regime: Dict[str, Any], strategy_direction: int, reasoning: List[str]
    ):
        if not isinstance(regime, dict):
            reasoning.append("Regime payload missing/invalid -- scoring as neutral (50).")
            return 50.0, 0

        regime_name = str(regime.get("regime", "UNKNOWN")).upper()
        favorable_direction = self.REGIME_DIRECTION.get(regime_name, 0)

        if strategy_direction == 0 or favorable_direction == 0:
            score = 60.0  # neutral regime, or strategy itself is flat
        elif strategy_direction == favorable_direction:
            score = 85.0
        else:
            score = 25.0

        reasoning.append(
            f"Regime '{regime_name}' (favors direction {favorable_direction}) vs strategy "
            f"direction {strategy_direction} -> regime score {score:.1f}."
        )

        return score, favorable_direction

    def _apply_options_penalty(
        self,
        combined_score: float,
        options: Optional[Dict[str, Any]],
        reasoning: List[str],
    ) -> float:
        if not isinstance(options, dict):
            return combined_score

        if options.get("viable") is False:
            reasoning.append("Options analysis marked NOT viable -- applying a 25-point penalty.")
            return max(0.0, combined_score - 25.0)

        iv = options.get("implied_volatility")
        if isinstance(iv, (int, float)) and iv > 0.75:
            reasoning.append(
                f"Implied volatility {iv:.2f} is extreme -- applying a 10-point caution penalty."
            )
            return max(0.0, combined_score - 10.0)

        return combined_score

    def _build_result(
        self,
        action: str,
        confidence: float,
        strategy: Dict[str, Any],
        regime: Dict[str, Any],
        reasoning: List[str],
        score_breakdown: Dict[str, Any],
        vetoed: bool,
        valuation: Optional[Dict[str, Any]],
    ) -> Dict[str, Any]:
        strategy_name = strategy.get("strategy", "UNKNOWN") if isinstance(strategy, dict) else "UNKNOWN"
        regime_name = regime.get("regime", "UNKNOWN") if isinstance(regime, dict) else "UNKNOWN"

        return {
            "action": action,
            "confidence": confidence,
            "strategy": strategy_name,
            "regime": regime_name,
            "reasoning": reasoning,
            "score_breakdown": score_breakdown,
            "vetoed": vetoed,
            "context": {
                "valuation": valuation,
            },
        }

    @staticmethod
    def _to_float(value: Any, default: float = 0.0) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default