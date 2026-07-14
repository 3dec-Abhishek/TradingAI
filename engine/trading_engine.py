"""
============================================================
Production Trading Engine (INTEGRATED)
============================================================

Author: Abhishek Pandey

Description:
    Central orchestration engine for the autonomous AI trading
    platform.

    This version builds on the earlier bug-fix pass and wires
    every previously-instantiated-but-unused component into the
    pipeline (UniverseManager, MarketScanner, MarketAgent,
    OpportunityEngine, PortfolioManager, StrategyOptimizer, and an
    expanded AdaptiveStrategyEngine), and extends several stages
    (AI review, decision, position sizing, execution, learning,
    reporting, lifecycle, exit) with additional context per the
    integration spec.

    Every change is marked `# FIX:` (correctness bug) or
    `# IMPROVEMENT:` (new integration). Class names, method names,
    stage order, comments, and report calls are preserved from the
    reviewed file; nothing was rewritten or simplified.

    Several dependency classes (PortfolioManager, MarketScanner,
    MarketAgent, OpportunityEngine, StrategyOptimizer,
    AdaptiveStrategyEngine, LearningEngine, PerformanceAnalyzer,
    DatabaseAnalyzer, TradeLifecycleManager, ExitManager) were not
    provided as source, so their real method names/signatures are
    unknown. Every integration with those classes goes through the
    `_extend_call` helper below, or explicit `hasattr`/`getattr`
    checks, so nothing breaks if a given method doesn't exist yet --
    see the TODO comments scattered through each stage, and the
    consolidated TODO list at the bottom of this docstring.

    Remaining TODOs requiring changes OUTSIDE this file:
    - PortfolioManager: needs one of manage/process/analyze/rebalance
      implemented to produce rebalance/cash/PnL/exposure info.
    - MarketScanner: needs a `scan(symbols)` method to produce raw
      market data ahead of MarketAgent enrichment.
    - MarketAgent: needs an `enrich(market_data)` method.
    - OpportunityEngine: needs one of process/select/filter/evaluate
      implemented for a final cross-opportunity pass after ranking.
    - UniverseManager: needs one of get_universe/get_watchlist/prepare
      implemented to manage the trading universe ahead of the raw scan.
    - AdaptiveStrategyEngine: needs adjust_thresholds /
      adjust_indicator_weights / adjust_stop_loss / adjust_take_profit /
      adjust_volatility_filter / tune_for_regime for expanded adaptation
      beyond confidence.
    - StrategyOptimizer: needs one of optimize/update_parameters/tune
      to persist updated strategy parameters across cycles.
    - AITradingAgent.analyze / DecisionAgent.analyze: should accept
      `options`, `regime`, `valuation`, `dynamic_risk` keyword
      arguments to actually use the extra context now being offered
      by `_extend_call` (currently silently ignored if unsupported).
    - AdaptivePositionSizer.calculate: should accept `premium`,
      `max_loss`, `implied_volatility`, `contract_multiplier`,
      `expected_reward`, `stop_loss_distance` keyword arguments.
    - ExecutionManager.execute: should consume the new
      `execution_context` dict (position, allocation, options,
      stop_loss, take_profit, metadata) instead of an empty dict.
    - TradeLifecycleManager: needs handlers for partial_fill /
      mark_pending / mark_submitted / modify_trade /
      update_trailing_stop / close_trade / cancel_trade /
      expire_trade / reject_trade to support the full lifecycle.
    - ExitManager.evaluate: should accept `regime`, `atr`,
      `trailing_stop`, `volatility`, `holding_time` keyword arguments.
    - LearningEngine.learn: should accept `was_rejected`, `ai_review`,
      `confidence`, `regime`, `risk` keyword arguments.
    - PerformanceAnalyzer.analyze / DatabaseAnalyzer.analyze: should
      accept the expanded keyword arguments passed in
      run_reporting_stage.

    Also unresolved (see AI/Decision stage comments): position sizing
    and portfolio allocation are computed *after* the AI review and
    decision stages in the current pipeline order, so they cannot be
    passed into those stages without reordering the pipeline -- which
    is out of scope for this pass.
============================================================
"""

# ==========================================================
# Standard Library
# ==========================================================

from datetime import datetime
from collections import defaultdict  # FIX: needed for stage_times
import traceback
import logging
import time  # FIX: used by run_stage(), was missing
import json  # FIX: used by shutdown(), was missing
import uuid  # FIX: used to generate engine_id, was missing
import inspect  # IMPROVEMENT: backs the _extend_call helper below

# ==========================================================
# Broker
# ==========================================================

from broker.paper_broker import PaperBroker

# ==========================================================
# Orders / Execution
# ==========================================================

from orders.order_manager import OrderManager
from execution.execution_manager import ExecutionManager

# ==========================================================
# Portfolio
# ==========================================================

from agents.portfolio_agent import PortfolioAgent
from monitoring.portfolio_monitor import PortfolioMonitor
from portfolio.portfolio_manager import PortfolioManager
from portfolio.portfolio_valuation import PortfolioValuation
from risk.portfolio_allocator import PortfolioAllocator

# ==========================================================
# Market
# ==========================================================

from agents.market_agent import MarketAgent
from market.market_scanner import MarketScanner
from market.universe_manager import UniverseManager
from market.universe_scanner import UniverseScanner
from market.regime_detector import MarketRegimeDetector

# ==========================================================
# Strategy
# ==========================================================

from agents.strategy_agent import StrategyAgent
from optimization.strategy_optimizer import StrategyOptimizer
from adaptive.adaptive_strategy import AdaptiveStrategyEngine

# ==========================================================
# Opportunity Engine
# ==========================================================

from analytics.opportunity_scanner import OpportunityScanner
from analytics.opportunity_ranker import OpportunityRanker
from opportunities.opportunity_engine import OpportunityEngine

# ==========================================================
# AI
# ==========================================================

from agents.ai_trading_agent import AITradingAgent
from agents.decision_agent import DecisionAgent

# ==========================================================
# Options
# ==========================================================

from options.options_chain import OptionsChain
from options.options_analyzer import OptionsAnalyzer

# ==========================================================
# Risk
# ==========================================================

from agents.risk_agent import RiskAgent
from risk.dynamic_risk import DynamicRiskEngine
from risk.position_sizer import PositionSizer
from risk.adaptive_position_sizer import AdaptivePositionSizer
from risk.exit_manager import ExitManager

# ==========================================================
# Trading Lifecycle
# ==========================================================

from trading.trade_lifecycle import TradeLifecycleManager
from trading.exit_executor import ExitExecutor

# ==========================================================
# Learning
# ==========================================================

from learning.performance_tracker import PerformanceTracker
from learning.strategy_tracker import StrategyTracker
from learning.learning_engine import LearningEngine

# ==========================================================
# Analytics
# ==========================================================

from analytics.performance_analyzer import PerformanceAnalyzer
from analytics.database_analyzer import DatabaseAnalyzer

# ==========================================================
# Reports
# ==========================================================

from reports.portfolio_report import generate_report
from reports.market_report import generate_market_report
from reports.strategy_report import generate_strategy_report
from reports.options_report import generate_options_report
from reports.risk_report import generate_risk_report
from reports.monitor_report import generate_monitor_report
from reports.ai_report import generate_ai_report
from reports.decision_report import generate_decision_report
from reports.trade_report import generate_trade_report
from reports.learning_report import generate_learning_report
from reports.intelligence_report import generate_intelligence_report
from reports.valuation_report import generate_valuation_report
from reports.dynamic_risk_report import generate_dynamic_risk_report
from reports.position_size_report import generate_position_size_report
from reports.exit_report import generate_exit_report
from reports.lifecycle_report import generate_lifecycle_report
from reports.exit_execution_report import generate_exit_execution_report
from reports.execution_report import generate_execution_report


class TradingEngine:
    """
    Production AI Trading Engine.

    Orchestrates the complete trading pipeline. Contains no
    business logic itself -- only wiring, sequencing, timing,
    and error handling.
    """

    def __init__(self):

        print("\nInitializing Production Trading Engine...\n")

        # =====================================================
        # ENGINE METADATA / STATS
        # FIX: these were referenced in statistics()/run_stage()/
        # shutdown() but never initialized anywhere -> AttributeError
        # at runtime. Added here.
        # =====================================================

        self.engine_id = str(uuid.uuid4())
        self.start_time = datetime.now()
        self.total_cycles = 0
        self.successful_cycles = 0
        self.failed_cycles = 0
        self.stage_times = defaultdict(float)

        # =====================================================
        # CORE
        # =====================================================

        self.broker = PaperBroker()

        self.order_manager = OrderManager(
            self.broker
        )

        self.execution_manager = ExecutionManager(
            self.order_manager
        )

        # =====================================================
        # PORTFOLIO
        # =====================================================

        self.portfolio_agent = PortfolioAgent(
            self.broker
        )

        self.portfolio_monitor = PortfolioMonitor()

        self.portfolio_manager = PortfolioManager()

        self.portfolio_allocator = PortfolioAllocator()

        self.valuation_engine = PortfolioValuation()

        # =====================================================
        # MARKET
        # =====================================================

        self.market_agent = MarketAgent()

        self.market_scanner = MarketScanner()

        self.universe_manager = UniverseManager()

        self.universe_scanner = UniverseScanner()

        self.regime_detector = MarketRegimeDetector()

        # =====================================================
        # STRATEGY
        # =====================================================

        self.strategy_agent = StrategyAgent()

        self.strategy_optimizer = StrategyOptimizer()

        self.adaptive_strategy = AdaptiveStrategyEngine()

        # =====================================================
        # AI
        # =====================================================

        self.ai_agent = AITradingAgent()

        self.decision_agent = DecisionAgent()

        # =====================================================
        # OPTIONS
        # =====================================================

        self.options_chain = OptionsChain()

        self.options_analyzer = OptionsAnalyzer()

        # =====================================================
        # OPPORTUNITY ENGINE
        # =====================================================

        self.opportunity_scanner = OpportunityScanner(
            market_agent=self.market_agent,
            strategy_agent=self.strategy_agent,
            regime_detector=self.regime_detector
        )

        self.opportunity_ranker = OpportunityRanker()

        self.opportunity_engine = OpportunityEngine()

        # =====================================================
        # RISK
        # =====================================================

        self.risk_agent = RiskAgent()

        self.dynamic_risk = DynamicRiskEngine()

        self.position_sizer = PositionSizer()

        self.adaptive_position_sizer = AdaptivePositionSizer()

        self.exit_manager = ExitManager()

        # =====================================================
        # TRADE MANAGEMENT
        # =====================================================

        self.lifecycle_manager = TradeLifecycleManager()

        self.exit_executor = ExitExecutor(
            self.order_manager
        )

        # =====================================================
        # LEARNING
        # =====================================================

        self.performance_tracker = PerformanceTracker()

        self.performance_analyzer = PerformanceAnalyzer()

        self.strategy_tracker = StrategyTracker(
            self.performance_tracker
        )

        self.learning_engine = LearningEngine(
            self.performance_tracker,
            self.strategy_tracker
        )

        # =====================================================
        # DATABASE ANALYTICS
        # =====================================================

        self.database_analyzer = DatabaseAnalyzer(
            self.performance_tracker.memory.database
        )

        print("Trading Engine Ready.")

    # =========================================================
    # SHARED HELPER: OPTIONAL CONTEXT EXTENSION
    # IMPROVEMENT: used throughout this file to add new optional
    # context (options, regime, valuation, dynamic risk, allocation
    # inputs, etc.) to existing dependency calls without assuming
    # those classes have already been extended to accept it.
    # Inspects `func`'s real signature and only forwards the extra
    # keyword arguments it actually declares; if inspection isn't
    # possible, or the extended call still raises TypeError, falls
    # back to the original minimal call. This is what makes every
    # "if supported" / "maintain backward compatibility" requirement
    # in the integration spec hold without hardcoding assumptions
    # about third-party class internals that weren't provided here.
    # =========================================================

    def _extend_call(self, func, base_args=(), base_kwargs=None, extra_kwargs=None):
        base_kwargs = base_kwargs or {}
        extra_kwargs = extra_kwargs or {}

        try:
            sig = inspect.signature(func)
            accepted_extra = {
                k: v for k, v in extra_kwargs.items() if k in sig.parameters
            }
        except (TypeError, ValueError):
            accepted_extra = {}

        if not accepted_extra:
            return func(*base_args, **base_kwargs)

        try:
            return func(*base_args, **base_kwargs, **accepted_extra)
        except TypeError:
            return func(*base_args, **base_kwargs)

    # =========================================================
    # STAGE TIMING WRAPPER
    # FIX: this existed in the original file but was never
    # actually called from run() -- meaning stage_times was
    # always empty and this whole method was dead code. run()
    # below now routes every stage through this wrapper.
    # =========================================================

    def run_stage(self, name, func, *args, **kwargs):
        """
        Execute a stage while measuring execution time.
        """

        print("\n" + "=" * 60)
        print(name.upper())
        print("=" * 60)

        start = time.time()

        result = func(*args, **kwargs)

        elapsed = time.time() - start

        self.stage_times[name] += elapsed

        print(f"{name} completed in {elapsed:.2f}s")

        return result

    # =========================================================
    # MAIN CYCLE
    # =========================================================

    def run(self):
        """
        Execute one complete autonomous trading cycle.
        """

        cycle_start = datetime.now()

        self.total_cycles += 1  # FIX: was never incremented

        print("\n" + "=" * 60)
        print("STARTING TRADING CYCLE")
        print(cycle_start.strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 60)

        try:

            portfolio = self.run_stage(
                "portfolio_stage", self.run_portfolio_stage
            )

            market_state = self.run_stage(
                "market_stage", self.run_market_stage
            )

            opportunity = self.run_stage(
                "opportunity_stage",
                self.run_opportunity_stage,
                portfolio,
                market_state
            )

            strategy = self.run_stage(
                "strategy_stage", self.run_strategy_stage, opportunity
            )

            options = self.run_stage(
                "options_stage",
                self.run_options_stage,
                opportunity,
                strategy
            )

            risk = self.run_stage(
                "risk_stage",
                self.run_risk_stage,
                portfolio,
                opportunity,
                strategy,
                options
            )

            # IMPROVEMENT: item 1 -- AI review now also receives
            # `options` so it has options/Greeks/premium/volatility
            # context available (see run_ai_stage).
            ai_review = self.run_stage(
                "ai_stage",
                self.run_ai_stage,
                portfolio,
                opportunity,
                strategy,
                risk,
                options
            )

            # IMPROVEMENT: item 2 -- decision stage now also receives
            # `options` so options/dynamic-risk/valuation context is
            # available (see run_decision_stage).
            decision = self.run_stage(
                "decision_stage",
                self.run_decision_stage,
                portfolio,
                opportunity,
                strategy,
                risk,
                ai_review,
                options
            )

            # IMPROVEMENT: item 3 -- position stage now also receives
            # `options` so option-derived sizing inputs are available
            # (see run_position_stage).
            position = self.run_stage(
                "position_stage",
                self.run_position_stage,
                portfolio,
                opportunity,
                decision,
                risk,
                options
            )

            # IMPROVEMENT: item 4 -- execution stage now also receives
            # `options` to build the structured execution context
            # (see run_execution_stage).
            trade = self.run_stage(
                "execution_stage",
                self.run_execution_stage,
                decision,
                opportunity,
                position,
                portfolio,  # FIX: pass existing portfolio_state instead
                            # of re-fetching from broker inside the stage
                options
            )

            self.run_stage(
                "lifecycle_stage", self.run_lifecycle_stage, trade
            )

            self.run_stage(
                "exit_stage", self.run_exit_stage, opportunity
            )

            # IMPROVEMENT: item 12 -- bundle everything the learning
            # stage might want beyond trade/decision (strategy, risk,
            # AI review, regime, options) into one context dict so it
            # can learn from rejected/skipped trades and AI overrides
            # too, not just fills.
            learning_context = {
                "strategy": strategy,
                "risk": risk,
                "ai_review": ai_review,
                "regime": opportunity["regime"],
                "options": options,
            }

            learning = self.run_stage(
                "learning_stage",
                self.run_learning_stage,
                trade,
                decision,
                learning_context
            )

            reports = self.run_stage(
                "reporting_stage",
                self.run_reporting_stage,
                portfolio=portfolio,
                market=market_state,  # FIX: was `opportunity` in the
                                      # original, mislabeled as "market"
                strategy=strategy,
                options=options,
                risk=risk,
                ai=ai_review,
                decision=decision,
                trade=trade,
                learning=learning
            )

            self.successful_cycles += 1  # FIX: was never incremented

            print("\n" + "=" * 60)
            print("TRADING CYCLE COMPLETE")
            print("=" * 60)

            return {
                "status": "SUCCESS",
                "cycle_time": (
                    datetime.now() - cycle_start
                ).total_seconds(),
                "portfolio": portfolio,
                "market": market_state,
                "strategy": strategy,
                "risk": risk,
                "ai": ai_review,
                "decision": decision,
                "trade": trade,
                "learning": learning,
                "reports": reports
            }

        except Exception as e:

            self.failed_cycles += 1  # FIX: was never incremented

            logging.exception(e)

            traceback.print_exc()

            return {
                "status": "FAILED",
                "error": str(e),
                "cycle_time": (
                    datetime.now() - cycle_start
                ).total_seconds()
            }

    # =========================================================
    # PORTFOLIO STAGE
    # =========================================================

    def run_portfolio_stage(self):
        """
        Analyze portfolio and account state.
        """

        portfolio = self.portfolio_agent.analyze()

        generate_report(portfolio)

        monitor = self.portfolio_monitor.analyze(portfolio)

        generate_monitor_report(monitor)

        valuation = self.valuation_engine.calculate(
            self.order_manager.account,
            portfolio.get("market_prices", {})
        )

        generate_valuation_report(valuation)

        # IMPROVEMENT: item 9 -- PortfolioManager was instantiated but
        # never used. Wire it in here to produce rebalance / cash
        # allocation / realized+unrealized PnL / exposure /
        # concentration / sector allocation info alongside the raw
        # portfolio snapshot, and hand it downstream to later stages.
        # Tries the most likely method names in order; if none exist
        # this is a documented no-op (`management` stays `{}`) -- see
        # the module docstring TODO list.
        management = {}
        for method_name in ("manage", "process", "analyze", "rebalance"):
            if hasattr(self.portfolio_manager, method_name):
                management = getattr(self.portfolio_manager, method_name)(portfolio)
                break
        # TODO: if PortfolioManager doesn't implement any of the above
        # yet, add one of them there to enable this integration.

        return {
            "portfolio": portfolio,
            "monitor": monitor,
            "valuation": valuation,
            "management": management  # IMPROVEMENT: new key, additive only
        }

    # =========================================================
    # MARKET STAGE
    # =========================================================

    def run_market_stage(self):
        """
        Scan the trading universe and identify market conditions.
        """

        # IMPROVEMENT: item 8 -- UniverseManager was instantiated but
        # never used. Give it first chance to maintain/prepare the
        # trading universe (watchlists, dynamic membership) before
        # the raw scanner runs. Falls back to the scanner's own
        # universe if the manager doesn't expose a universe-producing
        # method yet.
        symbols = None
        for method_name in ("get_universe", "get_watchlist", "prepare"):
            if hasattr(self.universe_manager, method_name):
                result = getattr(self.universe_manager, method_name)()
                if result:
                    symbols = result
                break
        # TODO: if UniverseManager doesn't implement any of the above
        # yet, add one of them there to enable this integration.

        if not symbols:
            symbols = self.universe_scanner.get_universe()

        # IMPROVEMENT: items 6 & 7 -- MarketScanner and MarketAgent
        # were both instantiated but never used directly (MarketAgent
        # was only passed as a dependency *into* OpportunityScanner).
        # Run MarketScanner over the prepared universe to get raw
        # market data, then let MarketAgent enrich it, before handing
        # it to the opportunity scan. Both steps are skipped cleanly
        # if the classes don't expose the expected method.
        market_data = None
        if hasattr(self.market_scanner, "scan"):
            market_data = self.market_scanner.scan(symbols)
        # TODO: if MarketScanner doesn't implement `scan` yet, add it
        # there to enable this integration.

        if market_data is not None and hasattr(self.market_agent, "enrich"):
            market_data = self.market_agent.enrich(market_data)
        # TODO: if MarketAgent doesn't implement `enrich` yet, add it
        # there to enable this integration.

        # IMPROVEMENT: pass the (possibly enriched) market_data into
        # the opportunity scan when the scanner's signature accepts
        # it; falls back to the original single-argument call
        # otherwise, so this is fully backward compatible.
        opportunities = self._extend_call(
            self.opportunity_scanner.scan,
            base_args=(symbols,),
            extra_kwargs={"market_data": market_data} if market_data is not None else {}
        )

        if not opportunities:
            raise RuntimeError("No trading opportunities found.")

        # FIX: opportunities were never actually ranked despite
        # OpportunityRanker existing and being instantiated in
        # __init__. Wire it in here so "best" reflects the ranker's
        # ordering rather than raw scanner order.
        opportunities = self.opportunity_ranker.rank(opportunities)

        # IMPROVEMENT: item 5 -- OpportunityEngine was instantiated
        # but never used. Give it a final cross-opportunity pass over
        # the ranked list (e.g. portfolio-aware selection/filtering)
        # if it exposes a method for that. Falls back to the ranked
        # list unchanged otherwise, so nothing is duplicated if the
        # engine doesn't yet implement this.
        for method_name in ("process", "select", "filter", "evaluate"):
            if hasattr(self.opportunity_engine, method_name):
                engine_result = getattr(self.opportunity_engine, method_name)(opportunities)
                if engine_result:
                    opportunities = engine_result
                break
        # TODO: if OpportunityEngine doesn't implement any of the
        # above yet, add one of them there to enable this integration.

        best = opportunities[0]

        market = best["market"]

        regime = self.regime_detector.analyze(market)

        generate_market_report(market)

        print(f"Selected Symbol : {market['symbol']}")
        print(f"Price           : {market['price']}")
        print(f"Regime          : {regime['regime']}")

        return {
            "market": market,
            "regime": regime,
            "opportunities": opportunities
        }

    # =========================================================
    # OPPORTUNITY STAGE
    # =========================================================

    def run_opportunity_stage(self, portfolio_state, market_state):
        """
        Select the highest-ranked opportunity from the market scan.
        """

        opportunities = market_state["opportunities"]

        if len(opportunities) == 0:
            raise RuntimeError("No opportunities available.")

        best = opportunities[0]

        market = best["market"]
        signal = best.get("signal", {})
        regime = best.get("regime", market_state["regime"])

        print(f"Selected Symbol : {market['symbol']}")
        print(f"Price           : {market['price']}")

        return {
            "market": market,
            "signal": signal,
            "regime": regime
        }

    # =========================================================
    # STRATEGY STAGE
    # =========================================================

    def run_strategy_stage(self, opportunity):
        """
        Execute all strategies against the selected opportunity.
        """

        market = opportunity["market"]

        signals = self.strategy_agent.analyze(market)

        if isinstance(signals, list):

            if len(signals) == 0:
                signals = {
                    "strategy": "NONE",
                    "signal": "HOLD",
                    "confidence": 0
                }
            else:
                signals = max(
                    signals,
                    key=lambda x: x.get("confidence", 0)
                )

        generate_strategy_report(signals)

        print(signals)

        return signals

    # =========================================================
    # OPTIONS STAGE
    # =========================================================

    def run_options_stage(self, opportunity, strategy):
        """
        Analyze the option chain for the selected opportunity.
        """

        market = opportunity["market"]

        chain = self.options_chain.get_chain(
            market["symbol"],
            market["price"]
        )

        options = self.options_analyzer.analyze(chain, market, strategy)

        generate_options_report(options)

        return options

    # =========================================================
    # RISK STAGE
    # =========================================================

    def run_risk_stage(self, portfolio_state, opportunity, strategy, options):
        """
        Perform pre-trade risk analysis.
        """

        portfolio = portfolio_state["portfolio"]
        market = opportunity["market"]

        # TODO: `trade_size` (1500) and `today_loss` (0) below are
        # placeholders that were hardcoded in the original file.
        # They should come from real portfolio/account state
        # (e.g. a configured sizing rule and the account's actual
        # realized P&L for the current session) rather than
        # constants. Left as-is here since the correct source
        # fields weren't available in the reviewed code, but this
        # is flagged as a correctness gap, not a style nit.
        proposed_trade = {
            "symbol": market["symbol"],
            "price": market["price"],
            "trade_size": 1500,
            "options_value": (
                options.get("recommended_cost", 0)
                if isinstance(options, dict)
                else 0
            ),
            "today_loss": 0
        }

        risk = self.risk_agent.analyze(portfolio, proposed_trade)

        dynamic_risk = self.dynamic_risk.analyze(
            portfolio_state["valuation"],
            proposed_trade
        )

        generate_risk_report(risk)
        generate_dynamic_risk_report(dynamic_risk)

        return {
            "risk": risk,
            "dynamic": dynamic_risk,
            "trade": proposed_trade
        }

    # =========================================================
    # AI REVIEW STAGE
    # =========================================================

    def run_ai_stage(self, portfolio_state, opportunity, strategy, risk_state, options):
        """
        Validate the trade using the LLM.
        """

        # IMPROVEMENT: item 1 -- extended per spec so the AI reviewer
        # has full context: options analysis, market regime, and
        # portfolio valuation, in addition to portfolio/market/
        # strategy/risk. This gives it what it needs to validate
        # options trades (volatility, Greeks, premium) and portfolio
        # exposure, not just the stock signal + risk numbers.
        #
        # TODO: position sizing was requested as optional additional
        # context here too, but in this pipeline position sizing is
        # computed *after* the decision stage (which is after AI
        # review) -- it doesn't exist yet at this point in the cycle.
        # Passing it would require reordering stages, which is out of
        # scope for this pass. Flagging as a known gap rather than
        # guessing at a value.
        ai = self._extend_call(
            self.ai_agent.analyze,
            base_args=(
                portfolio_state["portfolio"],
                opportunity["market"],
                strategy,
                risk_state["risk"],
            ),
            extra_kwargs={
                "options": options,
                "regime": opportunity["regime"],
                "valuation": portfolio_state["valuation"],
            }
        )

        generate_ai_report(ai)

        return ai

    # =========================================================
    # DECISION STAGE
    # =========================================================

    def run_decision_stage(
        self, portfolio_state, opportunity, strategy, risk_state, ai_review, options
    ):
        """
        Merge strategy, AI and risk into one decision.
        """

        signals = dict(strategy)

        strategy_name = signals.get("strategy", "UNKNOWN")

        # FIX: original referenced self.adaptive_engine, which does
        # not exist -- __init__ creates self.adaptive_strategy. This
        # was a guaranteed AttributeError at runtime.
        signals["confidence"] = self.adaptive_strategy.adjust_confidence(
            strategy_name,
            signals.get("confidence", 50)
        )

        # IMPROVEMENT: item 11 -- expand AdaptiveStrategyEngine usage
        # beyond confidence adjustment when the class supports it
        # (thresholds, indicator weights, stop loss, take profit,
        # volatility filters, regime-specific tuning). Purely
        # additive/defensive: only calls methods that actually exist.
        for method_name, key in (
            ("adjust_thresholds", "thresholds"),
            ("adjust_indicator_weights", "indicator_weights"),
            ("adjust_stop_loss", "stop_loss"),
            ("adjust_take_profit", "take_profit"),
            ("adjust_volatility_filter", "volatility_filter"),
            ("tune_for_regime", "regime_tuning"),
        ):
            if hasattr(self.adaptive_strategy, method_name):
                signals[key] = getattr(self.adaptive_strategy, method_name)(
                    strategy_name, opportunity["regime"]
                )
            # TODO: if AdaptiveStrategyEngine doesn't implement
            # `method_name` yet, add it there to enable this hook.

        # IMPROVEMENT: item 2 -- give the decision agent options
        # analysis, dynamic risk, and portfolio valuation in addition
        # to strategy/risk/AI/regime, so the final decision reflects
        # everything computed so far in the cycle.
        #
        # TODO: portfolio *allocation* was also requested here, but
        # allocation is computed in the position-sizing stage, which
        # runs *after* this decision stage in the current pipeline
        # order -- it genuinely doesn't exist yet at this point.
        # Can't be passed without reordering stages (out of scope).
        # Left as a known gap.
        decision = self._extend_call(
            self.decision_agent.analyze,
            base_args=(
                portfolio_state["portfolio"],
                opportunity["market"],
                signals,
                risk_state["risk"],
                ai_review,
                opportunity["regime"],
            ),
            extra_kwargs={
                "options": options,
                "dynamic_risk": risk_state["dynamic"],
                "valuation": portfolio_state["valuation"],
            }
        )

        generate_decision_report(decision)

        return decision

    # =========================================================
    # POSITION SIZING STAGE
    # FIX: this method was defined TWICE in the original file.
    # Python silently uses the second definition, making the first
    # one dead code. Kept only one version here (the one that
    # correctly downgrades the decision to HOLD when allocation
    # is not approved).
    # =========================================================

    def run_position_stage(self, portfolio_state, opportunity, decision, risk_state, options):
        """
        Calculate adaptive position size and verify portfolio allocation.
        """

        valuation = portfolio_state["valuation"]
        market = opportunity["market"]

        # IMPROVEMENT: item 3 -- pass additional options-derived
        # sizing inputs (premium, max loss, implied volatility,
        # contract multiplier, expected reward, stop loss distance)
        # through to AdaptivePositionSizer only when those fields are
        # actually present in the options analysis, and only if the
        # sizer's signature accepts them (_extend_call). Backward
        # compatible: falls back to the original four-argument call
        # otherwise.
        extra_sizing_context = {}
        if isinstance(options, dict):
            for field in (
                "premium", "max_loss", "implied_volatility",
                "contract_multiplier", "expected_reward", "stop_loss_distance",
            ):
                if field in options:
                    extra_sizing_context[field] = options[field]

        position = self._extend_call(
            self.adaptive_position_sizer.calculate,
            base_kwargs={
                "portfolio_value": valuation["portfolio_value"],
                "price": market["price"],
                "confidence": decision["confidence"],
                "regime": decision["regime"],
                "risk_status": risk_state["risk"]["status"],
            },
            extra_kwargs=extra_sizing_context
        )

        allocation = self.portfolio_allocator.evaluate_allocation(
            portfolio_state["portfolio"],
            decision,
            position
        )

        if not allocation["approved"]:

            decision["action"] = "HOLD"

            reason = allocation.get("reason", [])

            if isinstance(reason, str):
                reason = [reason]

            decision.setdefault("reason", [])
            decision["reason"].extend(reason)

        decision["quantity"] = position["quantity"]
        decision["allocation"] = position["allocation"]
        decision["position_value"] = position["position_value"]

        generate_position_size_report(position)

        return {
            "position": position,
            "allocation": allocation
        }

    # =========================================================
    # EXECUTION STAGE
    # =========================================================

    def run_execution_stage(self, decision, opportunity, position_state, portfolio_state, options):
        """
        Execute the approved trade.
        """

        allocation = position_state["allocation"]

        if not allocation["approved"]:

            decision["action"] = "HOLD"

            reasons = allocation.get("reason", [])

            if isinstance(reasons, str):
                reasons = [reasons]

            decision.setdefault("reason", [])
            decision["reason"].extend(reasons)

        # IMPROVEMENT: item 4 -- the original call passed an empty
        # dict as ExecutionManager's final argument. Replaced with a
        # structured execution context carrying what downstream
        # execution actually needs: position sizing, option info, and
        # stop loss / take profit if the decision or options analysis
        # provide them, plus basic trade/execution metadata for audit
        # trails.
        #
        # TODO: verify against ExecutionManager.execute's real
        # signature -- if it doesn't consume this shape yet, it needs
        # to be updated on that class to read `execution_context` (or
        # the specific fields inside it it cares about).
        execution_context = {
            "position": position_state["position"],
            "allocation": allocation,
            "options": options if isinstance(options, dict) else {},
            "stop_loss": decision.get("stop_loss") or (
                options.get("stop_loss") if isinstance(options, dict) else None
            ),
            "take_profit": decision.get("take_profit") or (
                options.get("take_profit") if isinstance(options, dict) else None
            ),
            "metadata": {
                "engine_id": self.engine_id,
                "cycle_time": datetime.now().isoformat(),
            },
        }

        trade = self.execution_manager.execute(
            decision,
            opportunity["market"],
            portfolio_state["portfolio"],  # FIX: reuse the portfolio
                                            # already computed this cycle
                                            # instead of calling
                                            # self.portfolio_agent.analyze()
                                            # a second time (redundant
                                            # broker round-trip / possible
                                            # inconsistency if state
                                            # changed between calls)
            allocation,
            execution_context  # IMPROVEMENT: was `{}` in the original
        )

        generate_execution_report(trade)

        generate_trade_report(trade)

        return trade

    # =========================================================
    # LIFECYCLE STAGE
    # =========================================================

    def run_lifecycle_stage(self, trade):
        """
        Register newly opened trades.
        """

        status = trade.get("status")

        # IMPROVEMENT: item 15 -- only "FILLED" was handled before.
        # Route other known lifecycle statuses to lifecycle_manager
        # if it exposes a matching method; each status maps to a
        # named handler so nothing is silently dropped, but a missing
        # handler is a documented no-op rather than a guess.
        status_handlers = {
            "FILLED": "open_trade",
            "PARTIALLY_FILLED": "partial_fill",
            "PENDING": "mark_pending",
            "SUBMITTED": "mark_submitted",
            "MODIFIED": "modify_trade",
            "TRAILING_STOP": "update_trailing_stop",
            "CLOSED": "close_trade",
            "CANCELLED": "cancel_trade",
            "EXPIRED": "expire_trade",
            "REJECTED": "reject_trade",
        }

        handler_name = status_handlers.get(status)

        if handler_name is None:
            return None

        if not hasattr(self.lifecycle_manager, handler_name):
            # TODO: TradeLifecycleManager does not yet implement
            # `handler_name` for status `status` -- add it there to
            # support this lifecycle state.
            return None

        lifecycle = getattr(self.lifecycle_manager, handler_name)(trade)

        generate_lifecycle_report(lifecycle)

        return lifecycle

    # =========================================================
    # EXIT MANAGEMENT STAGE
    # =========================================================

    def run_exit_stage(self, opportunity):
        """
        Evaluate exits for existing positions.
        """

        symbol = opportunity["market"]["symbol"]

        if symbol not in self.order_manager.account.positions:
            return None

        position = self.order_manager.account.positions[symbol]

        # IMPROVEMENT: item 16 -- pass additional exit context
        # (regime, plus ATR/trailing-stop/volatility/holding-time if
        # they're present on the position) through to
        # ExitManager.evaluate when it accepts them. Falls back to
        # the original two-argument call otherwise.
        extra_exit_context = {"regime": opportunity.get("regime")}
        for field in ("atr", "trailing_stop", "volatility", "holding_time"):
            if isinstance(position, dict) and field in position:
                extra_exit_context[field] = position[field]

        exit_signal = self._extend_call(
            self.exit_manager.evaluate,
            base_args=(position, opportunity["market"]["price"]),
            extra_kwargs=extra_exit_context
        )

        generate_exit_report(exit_signal)

        if exit_signal.get("action") == "SELL":

            result = self.exit_executor.execute_exit(
                exit_signal,
                symbol,
                opportunity["market"]["price"],
                position["quantity"]
            )

            generate_exit_execution_report(result)

            return result

        return exit_signal

    # =========================================================
    # LEARNING STAGE
    # FIX: run() called self.run_learning_stage(...) in the original
    # file, but the method was never defined anywhere in the class.
    # This was a guaranteed AttributeError on every single cycle.
    # Implemented using the learning modules that were already
    # instantiated in __init__ but otherwise unused.
    # =========================================================

    def run_learning_stage(self, trade, decision, learning_context=None):
        """
        Feed the outcome of this cycle back into the learning system.
        """

        learning_context = learning_context or {}

        self.performance_tracker.record(trade, decision)

        strategy_performance = self.strategy_tracker.update(
            decision.get("strategy"),
            trade
        )

        # IMPROVEMENT: item 12 -- feed rejected/skipped-trade info, AI
        # overrides, confidence, and regime/risk context into the
        # learning engine when it accepts them, not just the raw
        # trade/decision (_extend_call keeps this backward compatible
        # if LearningEngine.learn hasn't been extended yet).
        learning_result = self._extend_call(
            self.learning_engine.learn,
            base_args=(trade, decision),
            extra_kwargs={
                "was_rejected": decision.get("action") == "HOLD",
                "ai_review": learning_context.get("ai_review"),
                "confidence": decision.get("confidence"),
                "regime": learning_context.get("regime"),
                "risk": learning_context.get("risk"),
            }
        )

        # IMPROVEMENT: item 10 -- run the strategy optimizer after
        # learning so updated strategy parameters can persist for the
        # next cycle. Only runs if the optimizer exposes one of the
        # likely method names; otherwise this is a documented no-op.
        optimized_params = None
        for method_name in ("optimize", "update_parameters", "tune"):
            if hasattr(self.strategy_optimizer, method_name):
                optimized_params = getattr(self.strategy_optimizer, method_name)(
                    strategy_performance
                )
                break
        # TODO: if StrategyOptimizer doesn't implement any of the
        # above yet, add one of them there so optimized parameters
        # can persist across cycles. Persisting `optimized_params`
        # itself (e.g. to disk/DB) is also outside this file's scope
        # and belongs in that class.

        generate_learning_report(learning_result)

        return {
            "strategy_performance": strategy_performance,
            "learning_result": learning_result,
            "optimized_params": optimized_params,  # IMPROVEMENT: new key, additive
        }

    # =========================================================
    # REPORTING STAGE
    # FIX: run() called self.run_reporting_stage(...) in the original
    # file, but the method was never defined anywhere in the class.
    # This was a guaranteed AttributeError on every single cycle.
    # Implemented using the analytics modules that were already
    # instantiated in __init__ but otherwise unused.
    # =========================================================

    def run_reporting_stage(
        self, portfolio, market, strategy, options, risk, ai, decision, trade, learning
    ):
        """
        Produce end-of-cycle analytics and intelligence reports.
        """

        # IMPROVEMENT: items 13 & 14 -- expand PerformanceAnalyzer and
        # DatabaseAnalyzer inputs beyond just the performance tracker,
        # using _extend_call so this stays backward compatible if
        # those classes haven't been extended yet.
        performance = self._extend_call(
            self.performance_analyzer.analyze,
            base_args=(self.performance_tracker,),
            extra_kwargs={
                "portfolio": portfolio,
                "trade_history": trade,
                "strategy_performance": (
                    learning.get("strategy_performance")
                    if isinstance(learning, dict) else None
                ),
                "ai_performance": ai,
                "decision_quality": decision,
            }
        )

        database_summary = self._extend_call(
            self.database_analyzer.analyze,
            extra_kwargs={
                "trades": trade,
                "ai_history": ai,
                "learning_history": learning,
                "strategy_history": strategy,
                "portfolio_history": portfolio,
            }
        )

        intelligence = generate_intelligence_report({
            "portfolio": portfolio,
            "market": market,
            "strategy": strategy,
            "options": options,
            "risk": risk,
            "ai": ai,
            "decision": decision,
            "trade": trade,
            "learning": learning,
            "performance": performance,
            "database": database_summary
        })

        return {
            "performance": performance,
            "database": database_summary,
            "intelligence": intelligence
        }

    # =========================================================
    # STATISTICS
    # =========================================================

    def statistics(self):
        """
        Engine runtime statistics.
        """

        uptime = (datetime.now() - self.start_time).total_seconds()

        return {
            "engine_id": self.engine_id,
            "uptime": uptime,
            "total_cycles": self.total_cycles,
            "successful_cycles": self.successful_cycles,
            "failed_cycles": self.failed_cycles,
            "success_rate": (
                0
                if self.total_cycles == 0
                else round(
                    self.successful_cycles / self.total_cycles * 100, 2
                )
            ),
            "stage_times": dict(self.stage_times)
        }

    # =========================================================
    # SHUTDOWN
    # =========================================================

    def shutdown(self):
        """
        Gracefully shutdown engine.
        """

        print("\n")
        print("=" * 60)
        print("ENGINE SHUTDOWN")
        print("=" * 60)

        print(json.dumps(self.statistics(), indent=4, default=str))