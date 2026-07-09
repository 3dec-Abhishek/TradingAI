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


from options.options_chain import OptionsChain
from options.options_analyzer import OptionsAnalyzer
from reports.options_report import generate_options_report


from reports.trade_report import generate_trade_report

from memory.trade_memory import TradeMemory
from reports.memory_report import generate_memory_report


def main():

    print("\nStarting Trading AI System...\n")


    # ==================================================
    # PAPER BROKER
    # ==================================================

    broker = PaperBroker()



    # ==================================================
    # PORTFOLIO AGENT
    # ==================================================

    portfolio_agent = PortfolioAgent(
        broker
    )


    portfolio = portfolio_agent.analyze()


    generate_report(
        portfolio
    )



    # ==================================================
    # MARKET AGENT
    # ==================================================

    market_agent = MarketAgent()


    market = market_agent.analyze_symbol(
        "AAPL"
    )


    generate_market_report(
        market
    )



    # ==================================================
    # STRATEGY AGENT
    # ==================================================

    strategy_agent = StrategyAgent()


    signals = strategy_agent.analyze(
        market
    )


    generate_strategy_report(
        signals
    )



    # ==================================================
    # OPTIONS ENGINE
    # ==================================================

    options_chain = OptionsChain()


    chain = options_chain.get_chain(

        market["symbol"],

        market["price"]

    )


    options_analyzer = OptionsAnalyzer()


    options = options_analyzer.analyze(

        chain,

        market,

        signals

    )


    generate_options_report(
        options
    )



    # ==================================================
    # RISK MANAGEMENT
    # ==================================================

    risk_agent = RiskAgent()


    proposed_trade = {

        "trade_size": 1500,

        "options_value": 2000,

        "today_loss": 250

    }


    risk = risk_agent.analyze(

        portfolio,

        proposed_trade

    )


    generate_risk_report(
        risk
    )



    # ==================================================
    # LOCAL LLM ANALYSIS
    # ==================================================

    ai_agent = AITradingAgent()


    ai_response = ai_agent.analyze(

        portfolio,

        market,

        signals

    )


    generate_ai_report(
        ai_response
    )



    # ==================================================
    # FINAL DECISION AGENT
    # ==================================================

    decision_agent = DecisionAgent()


    decision = decision_agent.analyze(

        portfolio,

        market,

        signals,

        risk,

        ai_response

    )


    generate_decision_report(
        decision
    )



    # ==================================================
    # PAPER TRADE EXECUTION
    # ==================================================

    order_manager = OrderManager(
        broker
    )


    trade_result = order_manager.execute(

        decision,

        market

    )


    generate_trade_report(
        trade_result
    )


# ==================================================
# TRADE MEMORY
# ==================================================

memory = TradeMemory()


memory.save_trade({

    "symbol": market["symbol"],

    "action": decision.get("action"),

    "confidence": decision.get("confidence"),

    "price": market["price"]

})


history = memory.get_history()


generate_memory_report(
    history
)


print("\nTrading AI Cycle Completed Successfully\n")



if __name__ == "__main__":

    main()