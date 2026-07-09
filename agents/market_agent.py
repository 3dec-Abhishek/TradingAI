from market.data_provider import MarketDataProvider
from market.market_analyzer import MarketAnalyzer



class MarketAgent:


    def __init__(self):

        self.provider = MarketDataProvider()

        self.analyzer = MarketAnalyzer()



    def analyze_symbol(
            self,
            symbol
        ):


        history = (
            self.provider
            .get_price_history(symbol)
        )


        result = (
            self.analyzer
            .analyze(history)
        )


        result["symbol"] = symbol


        return result
