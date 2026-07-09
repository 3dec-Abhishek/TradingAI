from broker.paper_broker import PaperBroker
from orders.order_manager import OrderManager

from agents.portfolio_agent import PortfolioAgent
from reports.portfolio_report import generate_report

from agents.market_agent import MarketAgent
from reports.market_report import generate_market_report

from agents.strategy_agent import StrategyAgent
from reports.strategy_report import generate_strategy_report

from agents.risk_agent import RiskAgent
from reports.risk_report import generate_risk_report

from agents.ai_trading_agent import AITradingAgent
from reports.ai_report import generate_ai_report

from agents.decision_agent import DecisionAgent
from reports.decision_report import generate_decision_report

from reports.trade_report import generate_trade_report



def main():

    print("\nStarting Trading AI System...\n")


    # =========================
    # Paper Broker
    # =========================

    broker = PaperBroker()



    # =========================
    # Portfolio Agent
    # =========================

    portfolio_agent = PortfolioAgent(
        broker
    )


    portfolio = (
        portfolio_agent
        .analyze()
    )


    generate_report(
        portfolio
    )



    # =========================
    # Market Agent
    # =========================

    market_agent = MarketAgent()


    market = (
        market_agent
        .analyze_symbol(
            "AAPL"
        )
    )


    generate_market_report(
        market
    )



    # =========================
    # Strategy Agent
    # =========================

    strategy_agent = StrategyAgent()


    signals = (
        strategy_agent
        .analyze(
            market
        )
    )


    generate_strategy_report(
        signals
    )



    # =========================
    # Risk Agent
    # =========================

    risk_agent = RiskAgent()


    proposed_trade = {

        "trade_size":1500,

        "options_value":2000,

        "today_loss":250

    }


    risk = risk_agent.analyze(

        portfolio,

        proposed_trade

    )


    generate_risk_report(
        risk
    )



    # =========================
    # Local AI Agent
    # =========================

    ai_agent = AITradingAgent()


    ai_response = (
        ai_agent
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
    # Decision Agent
    # =========================

    decision_agent = DecisionAgent()


    decision = (
        decision_agent
        .analyze(

            portfolio,

            market,

            signals,

            risk,

            ai_response

        )
    )


    generate_decision_report(
        decision
    )



    # =========================
    # Paper Trade Execution
    # =========================

    order_manager = OrderManager(
        broker
    )


    trade_result = (
        order_manager
        .execute(

            decision,

            market

        )
    )


    generate_trade_report(
        trade_result
    )



if __name__ == "__main__":

    main()