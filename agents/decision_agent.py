class DecisionAgent:

    def __init__(self):
        pass

    def analyze(
        self,
        portfolio,
        market,
        signals,
        risk,
        ai_response,
        regime=None
    ):

        symbol = market.get("symbol", "UNKNOWN")

        confidence = 50
        reasons = []

        strategy = "UNKNOWN"
        strategy_action = "HOLD"

        # =====================================
        # Parse Strategy Signals
        # =====================================

        if isinstance(signals, list):

            buy_votes = 0
            sell_votes = 0

            for signal in signals:

                strategy = signal.get(
                    "strategy",
                    strategy
                )

                action = signal.get(
                    "signal",
                    signal.get(
                        "action",
                        "HOLD"
                    )
                )

                conf = signal.get(
                    "confidence",
                    50
                )

                confidence += int(conf * 0.20)

                if action == "BUY":
                    buy_votes += 1

                elif action == "SELL":
                    sell_votes += 1

            if buy_votes > sell_votes:
                strategy_action = "BUY"

            elif sell_votes > buy_votes:
                strategy_action = "SELL"

            else:
                strategy_action = "HOLD"

        elif isinstance(signals, dict):

            strategy = signals.get(
                "strategy",
                "UNKNOWN"
            )

            strategy_action = signals.get(
                "action",
                signals.get(
                    "signal",
                    "HOLD"
                )
            )

            confidence += int(
                signals.get(
                    "confidence",
                    50
                ) * 0.20
            )

        # =====================================
        # Strategy Confidence
        # =====================================

        if strategy_action == "BUY":

            confidence += 15
            reasons.append(
                "Strategy favors BUY"
            )

        elif strategy_action == "SELL":

            confidence += 15
            reasons.append(
                "Strategy favors SELL"
            )

        else:

            confidence -= 5
            reasons.append(
                "No strong strategy signal"
            )

        # =====================================
        # Risk
        # =====================================

        risk_status = str(
            risk.get(
                "status",
                ""
            )
        ).upper()

        if risk_status in ["FAIL", "FAILED", "REJECTED"]:

            confidence -= 40

            reasons.append(
                "Risk rejected trade"
            )

        elif risk_status in ["PASS", "APPROVED"]:

            confidence += 10

            reasons.append(
                "Risk approved"
            )

        # =====================================
        # AI Recommendation
        # =====================================

        if isinstance(ai_response, dict):

            ai_action = ai_response.get(
                "action",
                "HOLD"
            )

            if ai_action == strategy_action:

                confidence += 5

                reasons.append(
                    "AI agrees with strategy"
                )

        # =====================================
        # Market Regime
        # =====================================

        if regime:

            market_regime = regime.get(
                "regime",
                "UNKNOWN"
            )

            if market_regime == "BULLISH":

                confidence += 10

                reasons.append(
                    "Bullish market regime"
                )

            elif market_regime == "BEARISH":

                confidence -= 20

                reasons.append(
                    "Bearish market regime"
                )

            elif market_regime == "HIGH_VOLATILITY":

                confidence -= 15

                reasons.append(
                    "High volatility"
                )

            elif market_regime == "SIDEWAYS":

                confidence -= 5

                reasons.append(
                    "Sideways market"
                )

        else:

            market_regime = "UNKNOWN"

        # =====================================
        # Clamp Confidence
        # =====================================

        confidence = max(
            0,
            min(
                100,
                confidence
            )
        )

        # =====================================
        # Final Action
        # =====================================

        if confidence < 60:

            action = "HOLD"

        else:

            action = strategy_action

        # =====================================
        # Return
        # =====================================

        return {

            "symbol": symbol,

            "action": action,

            "strategy": strategy,

            "confidence": confidence,

            "regime": market_regime,

            "reason": reasons

        }