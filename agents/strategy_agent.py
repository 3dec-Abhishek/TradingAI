from strategies.strategy_engine import StrategyEngine



class StrategyAgent:


    def __init__(self):

        self.engine = StrategyEngine()



    def analyze(self, market_data):

        return (
            self.engine
            .evaluate(
                market_data
            )
        )
