from strategies.strategy_generator import StrategyGenerator
from strategies.strategy_validator import StrategyValidator



class StrategyFactory:



    def __init__(self):

        self.generator = StrategyGenerator()

        self.validator = StrategyValidator()



    def create(self):


        strategies = (
            self.generator.generate()
        )


        return strategies