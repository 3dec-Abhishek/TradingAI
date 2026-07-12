from strategies.strategy_engine import StrategyEngine
from core.validator import DataValidator


class StrategyAgent:


    def __init__(self):

        self.engine = StrategyEngine()



    def analyze(self, market_data):


        result = self.engine.evaluate(
            market_data
        )


        return DataValidator.ensure_signal(
            result
        )
