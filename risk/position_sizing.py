from risk.config import MAX_POSITION_PERCENT


class PositionSizer:

    def calculate(self, portfolio_value):

        return portfolio_value * MAX_POSITION_PERCENT