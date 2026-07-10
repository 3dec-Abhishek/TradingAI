from broker.paper_broker import PaperBroker


from agents.portfolio_agent import PortfolioAgent
from agents.market_agent import MarketAgent
from agents.strategy_agent import StrategyAgent
from agents.risk_agent import RiskAgent
from agents.ai_trading_agent import AITradingAgent
from agents.decision_agent import DecisionAgent


from orders.order_manager import OrderManager


from options.options_chain import OptionsChain
from options.options_analyzer import OptionsAnalyzer


from monitoring.portfolio_monitor import PortfolioMonitor


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





class TradingEngine:



    def __init__(self):


        print(
            "\nInitializing Trading Engine...\n"
        )



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


        self.strategy_agent = StrategyAgent()


        self.risk_agent = RiskAgent()


        self.ai_agent = AITradingAgent()


        self.decision_agent = DecisionAgent()



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
        # Learning System
        # =========================

        self.performance_tracker = PerformanceTracker()



        self.strategy_tracker = StrategyTracker(

            self.performance_tracker

        )



        self.learning_engine = LearningEngine(

            self.performance_tracker,

            self.strategy_tracker

        )



        # =========================
        # Database Intelligence
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



        # =========================
        # Market
        # =========================

        market = self.market_agent.analyze_symbol(

            "AAPL"

        )


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
        # Portfolio Monitor
        # =========================

        monitor = self.portfolio_monitor.analyze(

            portfolio

        )


        generate_monitor_report(

            monitor

        )



        # =========================
        # AI Analysis
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
        # Learning Data
        # =========================

        history = self.performance_tracker.get_history()



        best_strategy = (

            self.strategy_tracker

            .get_best_strategy()

        )



        # =========================
        # Decision
        # =========================

        decision = self.decision_agent.analyze(

            portfolio,

            market,

            signals,

            risk,

            ai_response,

            monitor,

            history,

            best_strategy

        )


        generate_decision_report(

            decision

        )



        # =========================
        # Execute
        # =========================

        trade_result = self.order_manager.execute(

            decision,

            market

        )


        generate_trade_report(

            trade_result

        )



        # =========================
        # Learning Update
        # =========================


        self.performance_tracker.record_trade(

            trade_result

        )



        strategy_name = decision.get(

            "strategy",

            "UNKNOWN"

        )



        self.strategy_tracker.record(

            strategy_name,

            trade_result

        )



        learning_result = self.learning_engine.analyze()



        generate_learning_report(

            learning_result

        )



        # =========================
        # Intelligence Report
        # =========================

        intelligence = self.database_analyzer.analyze()



        generate_intelligence_report(

            intelligence

        )



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


            "decision":

            decision,


            "trade":

            trade_result,


            "learning":

            learning_result,


            "intelligence":

            intelligence

        }