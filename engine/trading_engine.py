from broker.paper_broker import PaperBroker

from orders.order_manager import OrderManager


from agents.portfolio_agent import PortfolioAgent
from agents.market_agent import MarketAgent
from agents.strategy_agent import StrategyAgent
from agents.risk_agent import RiskAgent
from agents.ai_trading_agent import AITradingAgent
from agents.decision_agent import DecisionAgent


from options.options_chain import OptionsChain
from options.options_analyzer import OptionsAnalyzer


from monitoring.portfolio_monitor import PortfolioMonitor


from portfolio.portfolio_valuation import PortfolioValuation


from risk.dynamic_risk import DynamicRiskEngine
from risk.position_sizer import PositionSizer
from risk.exit_manager import ExitManager


from trading.trade_lifecycle import TradeLifecycleManager
from trading.exit_executor import ExitExecutor


from learning.performance_tracker import PerformanceTracker
from learning.strategy_tracker import StrategyTracker
from learning.learning_engine import LearningEngine


from analytics.database_analyzer import DatabaseAnalyzer



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
from analytics.performance_analyzer import PerformanceAnalyzer
from optimization.strategy_optimizer import StrategyOptimizer
from adaptive.adaptive_strategy import AdaptiveStrategyEngine
from market.regime_detector import MarketRegimeDetector
from risk.adaptive_position_sizer import AdaptivePositionSizer
from risk.portfolio_allocator import PortfolioAllocator
from market.universe_manager import UniverseManager
from analytics.opportunity_ranker import OpportunityRanker

class TradingEngine:


    def __init__(self):

        print("\nInitializing Trading Engine...\n")


        # =========================
        # Broker
        # =========================

        self.broker = PaperBroker()



        # =========================
        # Agents
        # =========================

        self.portfolio_agent = PortfolioAgent(
            self.broker
        )

        self.market_agent = MarketAgent()
        self.universe = UniverseManager()

        self.regime_detector = MarketRegimeDetector()

        self.strategy_agent = StrategyAgent()

        self.risk_agent = RiskAgent()

        self.ai_agent = AITradingAgent()

        self.decision_agent = DecisionAgent()
        self.portfolio_allocator = PortfolioAllocator()
        self.opportunity_ranker = OpportunityRanker()



        # =========================
        # Execution
        # =========================

        self.order_manager = OrderManager(
            self.broker
        )



        # =========================
        # Options
        # =========================

        self.options_chain = OptionsChain()

        self.options_analyzer = OptionsAnalyzer()



        # =========================
        # Monitoring
        # =========================

        self.portfolio_monitor = PortfolioMonitor()



        # =========================
        # Portfolio
        # =========================

        self.valuation_engine = PortfolioValuation()



        # =========================
        # Risk
        # =========================

        self.dynamic_risk = DynamicRiskEngine()
        self.adaptive_position_sizer = AdaptivePositionSizer()
        self.exit_manager = ExitManager()



        # =========================
        # Trading Lifecycle
        # =========================

        self.lifecycle_manager = TradeLifecycleManager()


        self.exit_executor = ExitExecutor(
            self.order_manager
        )



        # =========================
        # Learning
        # =========================

        self.performance_tracker = PerformanceTracker()

        self.performance_analyzer = PerformanceAnalyzer(
        )     
        self.strategy_optimizer = StrategyOptimizer()
        self.adaptive_engine = AdaptiveStrategyEngine()
        self.strategy_tracker = StrategyTracker(
            self.performance_tracker
        )


        self.learning_engine = LearningEngine(

            self.performance_tracker,

            self.strategy_tracker

        )



        # =========================
        # Intelligence
        # =========================

        self.database_analyzer = DatabaseAnalyzer(

            self.performance_tracker.memory.database

        )





    def run(self):


        print(
            "Starting Trading Cycle...\n"
        )


        # =========================
        # Portfolio
        # =========================


        portfolio = self.portfolio_agent.analyze()


        generate_report(
            portfolio
        )
        monitor=self.portfolio_monitor.analyze(portfolio)
        generate_monitor_report(
            monitor
        )

        # =========================
        # Market
        # =========================


        market = []
        for symbol in self.universe.get_symbols():
            market.append(self.market_agent.analyze(symbol))

        regime = self.regime_detector.analyze(market)
        print("\n")
        print("="* 50)
        print("MARKET REGIME")
        print("="* 50)
        print(f"Market Regime: {regime}")
        print("DESCRIPTION:", self.regime_detector.get_regime_description(regime))
        print("="* 50)


        generate_market_report(
            market
        )



        # =========================
        # Strategy
        # =========================


        signals = self.strategy_agent.analyze(

            market

        )


        generate_strategy_report(

            signals

        )



        # =========================
        # Options
        # =========================


        chain = self.options_chain.get_chain(

            market["symbol"],

            market["price"]

        )


        options = self.options_analyzer.analyze(

            chain,

            market,

            signals

        )


        generate_options_report(
            options
        )



        # =========================
        # Risk
        # =========================


        proposed_trade = {

            "trade_size":1500,

            "options_value":2000,

            "today_loss":250

        }


        risk = self.risk_agent.analyze(

            portfolio,

            proposed_trade

        )


        generate_risk_report(
            risk
        )



        # =========================
        # AI
        # =========================


        ai_response = self.ai_agent.analyze(

            portfolio,

            market,

            signals

        )


        generate_ai_report(
            ai_response
        )



        # =========================
        # Decision
        # =========================

        strategy_name = signals.get("strategy", "UNKNOWN")
        original_confidence = signals.get("confidence", 50)
        adaptive_confidence = self.adaptive_engine.adjust_confidence(
            strategy_name,
            original_confidence
        )
        signals["confidence"] = adaptive_confidence

        decision = self.decision_agent.analyze(

            portfolio,

            market,

            signals,

            risk,

            ai_response,
            regime
        )

        score = self.opportunity_ranker.score(

            market,

            signals,

            decision,

            regime

        )
        opportunities= [{
            "symbol": market["symbol"],
            "score": score,
            "decision": decision
        }]
        ranking = self.opportunity_ranker.rank(opportunities)

        print("\n")
        print("="* 50)
        print("OPPORTUNITY RANKING")
        print("="* 50)
        for i, item in enumerate(ranking, start=1):
            print(f"{i}.{item['symbol']} - Score: {item['score']}")
            print("="* 50)

        generate_decision_report(

            decision

        )



        # =========================
        # Valuation
        # =========================


        valuation = self.valuation_engine.calculate(

            self.order_manager.account,

            {

                market["symbol"]:
                market["price"]

            }

        )


        generate_valuation_report(

            valuation

        )



        # =========================
        # Dynamic Risk
        # =========================


        dynamic_risk = self.dynamic_risk.analyze(

            valuation,

            proposed_trade

        )


        generate_dynamic_risk_report(

            dynamic_risk

        )



        # =========================
        # Position Sizing
        # =========================


        position_size = self.adaptive_position_sizer.calculate(

            portfolio_value=valuation["portfolio_value"],
            price=market["price"],
            confidence=decision["confidence"],
            regime=decision["regime"],
            risk_status=risk["status"]

        )


        generate_position_size_report(

            position_size

        )


        decision["quantity"] = position_size["quantity"]
        decision["position_value"] = position_size["position_value"]
        decision["allocation"] = position_size["allocation"]

        allocation = self.portfolio_allocator.evaluate_allocation(
            portfolio,
            decision,
            position_size
        )
        if not allocation["approved"]:
            decision["action"]= "HOLD"
            decision["reasons"].extend(allocation["reason"])

            print("\n")
            print("="* 50)
            print("PORTFOLIO ALLOCATION")
            print("="* 50)
            print(allocation)
            print("=" * 50)

        print("\n")
        print("="* 50)
        print("ADAPTIVE POSITION SIZING")
        print("="* 50)
        print("Allocation:", f"{position_size['allocation']}%")
        print("Shares:",position_size["quantity"])
        print("Capital",f"${position_size['position_value']}")




        # =========================
        # Execute Entry
        # =========================


        trade_result = self.order_manager.execute(

            decision,

            market

        )


        generate_trade_report(

            trade_result

        )



        # =========================
        # Lifecycle Tracking
        # =========================


        if trade_result.get("status") == "FILLED":


            lifecycle = self.lifecycle_manager.open_trade(

                trade_result

            )


            generate_lifecycle_report(

                lifecycle

            )



        # =========================
        # Exit Management
        # =========================


        symbol = market["symbol"]



        if symbol in self.order_manager.account.positions:


            position = self.order_manager.account.positions[symbol]



            exit_signal = self.exit_manager.evaluate(

                position,

                market["price"]

            )


            generate_exit_report(

                exit_signal

            )



            # Automatic SELL

            if exit_signal.get("action") == "SELL":


                exit_result = self.exit_executor.execute_exit(

                    exit_signal,

                    symbol,

                    market["price"],

                    position["quantity"]

                )


                generate_exit_execution_report(

                    exit_result

                )



        # =========================
        # Learning
        # =========================


        self.performance_tracker.record_trade(

            trade_result
        )

        self.performance_analyzer.add_trade(
            trade_result
        )

        performance=self.performance_analyzer.analyze()

        # self.strategy_tracker.record(
        #     decision.get("strategy", "UNKNOWN"),trade_result
        # )

        strategy_name = decision.get("strategy", "UNKNOWN")
        self.strategy_tracker.record(strategy_name, trade_result)
        self.strategy_optimizer.record(strategy_name, trade_result)

        strategy_analysis = self.strategy_optimizer.analyze()
        adaptive_weights = self.adaptive_engine.update_weights(strategy_analysis)
        best_strategy = self.strategy_optimizer.get_best_strategy()

        learning = self.learning_engine.analyze()
        print("\n")
        print("="* 50)
        print("PERFORMANCE ANALYSIS")
        print("="* 50)

        for key, value in performance.items():
            print(f"{key}: {value}")
            print("=" * 50)

        generate_learning_report(

            learning

        )
        print("\n")
        print("="* 50)
        print("STRATEGY OPTIMIZATION")
        print("="* 50)

        for strategy, data in strategy_analysis.items():
            print(f"Strategy: {strategy}")
            print(data)
            print("BEST STRATEGY:", best_strategy)
            print("=" * 50)

        intelligence = self.database_analyzer.analyze()



        generate_intelligence_report(

            intelligence

        )

        print("\n")
        print("="* 50)
        print("ADAPTIVE STRATEGY WEIGHTS")
        print("="* 50)
        for strategy, weight in adaptive_weights.items():
            print(f"Strategy: {strategy}, Weight: {weight}")
            print("=" * 50)



        print(
            "\n=================================================="
        )

        print(
            "TRADING CYCLE COMPLETE"
        )

        print(
            "=================================================="
        )



        return {

            "decision": decision,

            "trade": trade_result,

            "valuation": valuation,

            "risk": dynamic_risk,

            "learning": learning,

            "performance": performance,

            "intelligence": intelligence

        }