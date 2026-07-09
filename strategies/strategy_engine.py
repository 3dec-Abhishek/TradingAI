from strategies.rsi_strategy import RSIStrategy
from strategies.moving_average_strategy import MovingAverageStrategy



class StrategyEngine:


    def __init__(self):

        self.strategies = [

            RSIStrategy(),

            MovingAverageStrategy()

        ]



    def evaluate(self, market_data):


        results = []


        for strategy in self.strategies:

            result = (
                strategy
                .analyze(
                    market_data
                )
            )

            results.append(result)


        return results
