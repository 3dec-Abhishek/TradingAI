from agents.portfolio_agent import PortfolioAgent


class PortfolioService:


    def __init__(self, broker):

        self.agent = PortfolioAgent(
            broker
        )


    def get_portfolio(self):

        return (

            self.agent
            .analyze()

        )