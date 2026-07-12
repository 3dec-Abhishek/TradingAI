from broker.paper_broker import PaperBroker

from orders.order_manager import OrderManager


# =========================
# Agents
# =========================

from agents.portfolio_agent import PortfolioAgent
from agents.market_agent import MarketAgent
from agents.strategy_agent import StrategyAgent
from agents.risk_agent import RiskAgent
from agents.ai_trading_agent import AITradingAgent
from agents.decision_agent import DecisionAgent


# =========================
# Market Intelligence
# =========================

from market.universe_manager import UniverseManager
from market.universe_scanner import UniverseScanner
from market.market_scanner import MarketScanner
from market.regime_detector import MarketRegimeDetector


# =========================
# Opportunities
# =========================

from opportunities.opportunity_engine import OpportunityEngine
from analytics.opportunity_ranker import OpportunityRanker
from analytics.opportunity_scanner import OpportunityScanner


# =========================
# Options
# =========================

from options.options_chain import OptionsChain
from options.options_analyzer import OptionsAnalyzer


# =========================
# Portfolio
# =========================

from portfolio.portfolio_valuation import PortfolioValuation
from portfolio.portfolio_manager import PortfolioManager


# =========================
# Risk
# =========================

from risk.dynamic_risk import DynamicRiskEngine
from risk.exit_manager import ExitManager
from risk.adaptive_position_sizer import AdaptivePositionSizer
from risk.portfolio_allocator import PortfolioAllocator


# =========================
# Execution
# =========================

from execution.execution_manager import ExecutionManager


# =========================
# Trading Lifecycle
# =========================

from trading.trade_lifecycle import TradeLifecycleManager
from trading.exit_executor import ExitExecutor


# =========================
# Learning
# =========================

from learning.performance_tracker import PerformanceTracker
from learning.strategy_tracker import StrategyTracker
from learning.learning_engine import LearningEngine


from analytics.performance_analyzer import PerformanceAnalyzer
from analytics.database_analyzer import DatabaseAnalyzer


# =========================
# Optimization
# =========================

from optimization.strategy_optimizer import StrategyOptimizer
from adaptive.adaptive_strategy import AdaptiveStrategyEngine



# =========================
# Reports
# =========================

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


# =========================
# Phase 17
# =========================

from monitoring.system_health import SystemHealth
from intelligence.intelligence_egine import IntelligenceEngine
from agents.voting_agent import VotingAgent

# phase 21

from risk.advanced_risk_engine import AdvancedRiskEngine

class TradingEngine:


    def __init__(self):

        print("\nInitializing Trading Engine...\n")


        # =========================
        # Broker
        # =========================

        self.broker = PaperBroker()



        # =========================
        # Core Agents
        # =========================

        self.portfolio_agent = PortfolioAgent(
            self.broker
        )


        self.market_agent = MarketAgent()


        self.strategy_agent = StrategyAgent()


        self.risk_agent = RiskAgent()


        self.ai_agent = AITradingAgent()


        self.decision_agent = DecisionAgent()

        self.voting_agent = VotingAgent()


        # =========================
        # Market Intelligence
        # =========================

        self.universe = UniverseManager()

        self.universe_scanner = UniverseScanner()

        self.market_scanner = MarketScanner()

        self.regime_detector = MarketRegimeDetector()



        # =========================
        # Opportunity Engine
        # =========================

        self.opportunity_scanner = OpportunityScanner(
            self.market_agent,
            self.strategy_agent,
            self.regime_detector
        )


        self.opportunity_ranker = OpportunityRanker()

        self.opportunity_engine = OpportunityEngine()

        self.intelligence_engine = IntelligenceEngine()



        # =========================
        # Portfolio Management
        # =========================

        self.position_manager = PortfolioManager()

        self.valuation_engine = PortfolioValuation()

        self.portfolio_allocator = PortfolioAllocator()



        # =========================
        # Options
        # =========================

        self.options_chain = OptionsChain()

        self.options_analyzer = OptionsAnalyzer()



        # =========================
        # Risk Management
        # =========================

        self.dynamic_risk = DynamicRiskEngine()

        self.advanced_risk = AdvancedRiskEngine()

        self.adaptive_position_sizer = AdaptivePositionSizer()

        self.exit_manager = ExitManager()



        # =========================
        # Order Execution
        # =========================

        self.order_manager = OrderManager(
            self.broker
        )


        self.execution_manager = ExecutionManager(
            self.order_manager
        )



        # =========================
        # Lifecycle
        # =========================

        self.lifecycle_manager = TradeLifecycleManager()


        self.exit_executor = ExitExecutor(
            self.order_manager
        )



        # =========================
        # Learning System
        # =========================

        self.performance_tracker = PerformanceTracker()


        self.performance_analyzer = PerformanceAnalyzer()


        self.strategy_tracker = StrategyTracker(
            self.performance_tracker
        )


        self.strategy_optimizer = StrategyOptimizer()


        self.adaptive_engine = AdaptiveStrategyEngine()



        self.learning_engine = LearningEngine(

            self.performance_tracker,

            self.strategy_tracker

        )



        # =========================
        # Intelligence Database
        # =========================

        self.database_analyzer = DatabaseAnalyzer(

            self.performance_tracker.memory.database

        )

        self.health = SystemHealth()


        print(
            "Trading Engine Initialized Successfully\n"
        )
    
    def run(self):


        print(
            "Starting Trading Cycle...\n"
        )

        print("\nSYSTEM HEALTH")
        print(self.health.check(self))

        # ==================================================
        # PORTFOLIO ANALYSIS
        # ==================================================

        portfolio = self.portfolio_agent.analyze()


        generate_report(
            portfolio
        )


        monitor = self.portfolio_monitor.analyze(
            portfolio
        )


        generate_monitor_report(
            monitor
        )



        # ==================================================
        # MARKET DISCOVERY
        # ==================================================

        print("\n")
        print("=" * 50)
        print("MARKET DISCOVERY")
        print("=" * 50)



        symbols = (
            self.universe_scanner.get_universe()
        )


        print(
            "Scanning symbols:",
            symbols
        )



        opportunities = (
            self.opportunity_scanner.scan(
                symbols
            )
        )



        if not opportunities:

            print(
                "No market opportunities found"
            )


            return {

                "status": "NO_OPPORTUNITY"

            }



        # Highest ranked opportunity

        best = (self.intelligence_engine.evaluate(opportunities))



        market = best.get(
            "market",
            {}
        )



        if not market:


            print(
                "Invalid market data"
            )


            return {

                "status":
                "INVALID_MARKET"

            }




        print("\n")
        print("=" * 50)
        print("SELECTED OPPORTUNITY")
        print("=" * 50)

        print(
            market.get(
                "symbol"
            )
        )

        print(
            market.get(
                "price"
            )
        )

        print("=" * 50)




        # ==================================================
        # MARKET REGIME
        # ==================================================


        regime = (
            self.regime_detector.analyze(
                market
            )
        )


        print("\n")
        print("=" * 50)
        print("MARKET REGIME")
        print("=" * 50)

        print(
            "REGIME:",
            regime.get(
                "regime"
            )
        )


        print(
            "PRICE:",
            regime.get(
                "price"
            )
        )


        print(
            "RSI:",
            regime.get(
                "rsi"
            )
        )


        print(
            "VOLATILITY:",
            regime.get(
                "volatility"
            )
        )


        print(
            "DESCRIPTION:",
            regime.get(
                "description"
            )
        )


        print("=" * 50)



        generate_market_report(
            market
        )



        # ==================================================
        # STRATEGY ANALYSIS
        # ==================================================

        signals = (
            self.strategy_agent.analyze(
                market
            )
        )



        if not isinstance(
            signals,
            dict
        ):


            signals = {

                "strategy":
                "UNKNOWN",


                "signal":
                "HOLD",


                "confidence":
                50

            }



        print(
            "STRATEGY:",
            signals
        )



        generate_strategy_report(
            signals
        )



        # ==================================================
        # OPTIONS ANALYSIS
        # ==================================================


        chain = (
            self.options_chain.get_chain(

                market["symbol"],

                market["price"]

            )
        )



        options = (
            self.options_analyzer.analyze(

                chain,

                market,

                signals

            )
        )



        generate_options_report(
            options
        )



        # ==================================================
        # RISK ANALYSIS
        # ==================================================


        proposed_trade = {


            "trade_size":
            1500,


            "options_value":
            2000,


            "today_loss":
            250


        }



        risk = (
            self.risk_agent.analyze(

                portfolio,

                proposed_trade

            )
        )


        generate_risk_report(
            risk
        )



        # ==================================================
        # AI ANALYSIS
        # ==================================================


        ai_response = (
            self.ai_agent.analyze(

                portfolio,

                market,

                signals

            )
        )


        generate_ai_report(
            ai_response
        )



        # ==================================================
        # FINAL DECISION
        # ==================================================


        strategy_name = (
            signals.get(
                "strategy",
                "UNKNOWN"
            )
        )



        confidence = (
            signals.get(
                "confidence",
                50
            )
        )



        confidence = (
            self.adaptive_engine.adjust_confidence(

                strategy_name,

                confidence

            )
        )



        signals["confidence"] = confidence

        vote = self.voting_agent.analyze(
            signals,
            ai_response,
            regime
        )
        signals["final_vote"] = vote

        advanced_risk = self.advanced_risk.analyze(

        portfolio,

        [market]

        )

        print("\n")
        print("="*50)
        print("ADVANCED RISK ANALYSIS")
        print("="*50)

        print(
        advanced_risk
        )

        print("="*50)



        decision = (
            self.decision_agent.analyze(

                portfolio,

                market,

                signals,

                risk,

                ai_response,

                regime

            )
        )

        if advanced_risk["control"]["status"] == "HALT":
            decision["action"] = "HOLD"

            decision["reasons"].append(
                "Advanced risk emergency shutdown"
            )

        generate_decision_report(
            decision
        )



        # ==================================================
        # VALUATION
        # ==================================================


        valuation = (
            self.valuation_engine.calculate(

                self.order_manager.account,


                {

                    market["symbol"]:
                    market["price"]

                }

            )
        )


        generate_valuation_report(
            valuation
        )



        # ==================================================
        # DYNAMIC RISK
        # ==================================================


        dynamic_risk = (
            self.dynamic_risk.analyze(

                valuation,

                proposed_trade

            )
        )


        generate_dynamic_risk_report(
            dynamic_risk
        )



        # ==================================================
        # POSITION SIZE
        # ==================================================


        position_size = (
            self.adaptive_position_sizer.calculate(

                portfolio_value =
                valuation["portfolio_value"],


                price =
                market["price"],


                confidence =
                decision["confidence"],


                regime =
                decision["regime"],


                risk_status =
                risk["status"]

            )
        )



        generate_position_size_report(
            position_size
        )



        decision.update({

            "quantity":
            position_size["quantity"],


            "position_value":
            position_size["position_value"],


            "allocation":
            position_size["allocation"]

        })



        allocation = (
            self.portfolio_allocator.evaluate_allocation(

                portfolio,

                decision,

                position_size

            )
        )



        if not allocation["approved"]:


            decision["action"] = "HOLD"


            decision.setdefault(
                "reason",
                []
            )


            decision["reason"].append(
                allocation["reason"]
            )



        print("\nPOSITION SIZE")

        print(
            position_size
        )
            # ==================================================
        # EXECUTION
        # ==================================================

        print("\n")
        print("=" * 50)
        print("EXECUTION")
        print("=" * 50)



        trade_result = (
            self.execution_manager.execute(

                decision,

                market,

                portfolio,

                allocation,

                risk

            )
        )



        generate_trade_report(
            trade_result
        )


        generate_execution_report(
            trade_result
        )



        print(
            trade_result
        )



        # ==================================================
        # TRADE LIFECYCLE
        # ==================================================

        if trade_result.get(
            "status"
        ) == "FILLED":


            lifecycle = (
                self.lifecycle_manager.open_trade(

                    trade_result

                )
            )


            generate_lifecycle_report(
                lifecycle
            )



        # ==================================================
        # EXIT MANAGEMENT
        # ==================================================

        symbol = (
            market.get(
                "symbol"
            )
        )



        if symbol in self.order_manager.account.positions:


            position = (
                self.order_manager.account.positions[symbol]
            )



            exit_signal = (
                self.exit_manager.evaluate(

                    position,

                    market["price"]

                )
            )


            generate_exit_report(
                exit_signal
            )



            if exit_signal.get(
                "action"
            ) == "SELL":



                exit_result = (
                    self.exit_executor.execute_exit(

                        exit_signal,

                        symbol,

                        market["price"],

                        position["quantity"]

                    )
                )



                generate_exit_execution_report(
                    exit_result
                )



        # ==================================================
        # LEARNING SYSTEM
        # ==================================================

        self.performance_tracker.record_trade(

            trade_result

        )



        self.performance_analyzer.add_trade(

            trade_result

        )



        performance = (
            self.performance_analyzer.analyze()
        )



        strategy_name = (
            decision.get(
                "strategy",
                "UNKNOWN"
            )
        )



        self.strategy_tracker.record(

            strategy_name,

            trade_result

        )



        self.strategy_optimizer.record(

            strategy_name,

            trade_result

        )



        strategy_analysis = (
            self.strategy_optimizer.analyze()
        )



        adaptive_weights = (
            self.adaptive_engine.update_weights(

                strategy_analysis

            )
        )



        # Safe optimizer call

        if hasattr(
            self.strategy_optimizer,
            "get_best_strategy"
        ):


            best_strategy = (
                self.strategy_optimizer.get_best_strategy()
            )

        else:

            best_strategy = "UNKNOWN"




        learning = (
            self.learning_engine.analyze()
        )



        print("\n")
        print("=" * 50)
        print("PERFORMANCE")
        print("=" * 50)



        for key, value in performance.items():

            print(
                key,
                ":",
                value
            )



        generate_learning_report(

            learning

        )



        print("\n")
        print("=" * 50)
        print("STRATEGY OPTIMIZATION")
        print("=" * 50)



        print(
            "BEST STRATEGY:",
            best_strategy
        )



        for strategy, data in strategy_analysis.items():

            print(
                strategy,
                data
            )



        print("\n")
        print("=" * 50)
        print("ADAPTIVE WEIGHTS")
        print("=" * 50)



        for strategy, weight in adaptive_weights.items():

            print(
                strategy,
                ":",
                weight
            )



        # ==================================================
        # DATABASE INTELLIGENCE
        # ==================================================

        intelligence = (
            self.database_analyzer.analyze()
        )



        generate_intelligence_report(

            intelligence

        )



        print("\n")
        print("=" * 50)
        print("TRADING CYCLE COMPLETE")
        print("=" * 50)



        return {


            "status":
            "COMPLETE",


            "symbol":
            market.get(
                "symbol"
            ),


            "decision":
            decision,


            "trade":
            trade_result,


            "valuation":
            valuation,


            "risk":
            dynamic_risk,


            "learning":
            learning,


            "performance":
            performance,


            "intelligence":
            intelligence

        }