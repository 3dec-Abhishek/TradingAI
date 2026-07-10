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


from reports.portfolio_report import generate_report
from reports.market_report import generate_market_report
from reports.strategy_report import generate_strategy_report
from reports.risk_report import generate_risk_report
from reports.ai_report import generate_ai_report
from reports.decision_report import generate_decision_report
from reports.trade_report import generate_trade_report
from reports.options_report import generate_options_report
from reports.monitor_report import generate_monitor_report




class TradingEngine:



    def __init__(self):


        print("\nInitializing Trading Engine...\n")


        self.broker = PaperBroker()



        self.portfolio_agent = PortfolioAgent(

            self.broker

        )


        self.market_agent = MarketAgent()


        self.strategy_agent = StrategyAgent()


        self.risk_agent = RiskAgent()


        self.ai_agent = AITradingAgent()


        self.decision_agent = DecisionAgent()


        self.order_manager = OrderManager(

            self.broker

        )


        self.options_chain = OptionsChain()


        self.options_analyzer = OptionsAnalyzer()


        self.portfolio_monitor = PortfolioMonitor()




    def run(self):


        print("Starting Trading Cycle...\n")



        # =========================
        # Portfolio
        # =========================


        portfolio = (

            self.portfolio_agent
            .analyze()

        )


        generate_report(

            portfolio

        )




        # =========================
        # Market
        # =========================


        market = (

            self.market_agent
            .analyze_symbol(

                "AAPL"

            )

        )


        generate_market_report(

            market

        )




        # =========================
        # Strategy
        # =========================


        signals = (

            self.strategy_agent
            .analyze(

                market

            )

        )


        generate_strategy_report(

            signals

        )




        # =========================
        # Options
        # =========================


        chain = (

            self.options_chain
            .get_chain(

                market["symbol"],

                market["price"]

            )

        )


        options = (

            self.options_analyzer
            .analyze(

                chain,

                market,

                signals

            )

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



        risk = (

            self.risk_agent
            .analyze(

                portfolio,

                proposed_trade

            )

        )


        generate_risk_report(

            risk

        )




        # =========================
        # Portfolio Monitor
        # =========================


        portfolio_health = (

            self.portfolio_monitor
            .analyze(

                portfolio

            )

        )


        generate_monitor_report(

            portfolio_health

        )




        # =========================
        # AI Analysis
        # =========================


        ai_response = (

            self.ai_agent
            .analyze(

                portfolio,

                market,

                signals

            )

        )


        generate_ai_report(

            ai_response

        )




        # =========================
        # Decision
        # =========================


        decision = (

            self.decision_agent
            .analyze(

                portfolio,

                market,

                signals,

                risk,

                ai_response,

                portfolio_health

            )

        )


        generate_decision_report(

            decision

        )




        # =========================
        # Execution
        # =========================


        trade_result = (

            self.order_manager
            .execute(

                decision,

                market

            )

        )


        generate_trade_report(

            trade_result

        )



        return {


            "decision":decision,


            "trade":trade_result


        }