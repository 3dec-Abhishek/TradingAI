from broker.mock_broker import MockBroker
from agents.portfolio_agent import PortfolioAgent
from reports.portfolio_report import generate_report



def main():

    broker = MockBroker()

    agent = PortfolioAgent(
        broker
    )

    result = agent.analyze()

    generate_report(result)



if __name__ == "__main__":
    main()
