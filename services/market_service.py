from agents.market_agent import MarketAgent


class MarketService:


    def __init__(self):

        self.agent = MarketAgent()



    def analyze_symbol(
        self,
        symbol
    ):

        return (

            self.agent
            .analyze_symbol(
                symbol
            )

        )