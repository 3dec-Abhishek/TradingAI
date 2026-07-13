class CapitalManager:

    def __init__(self):

        self.max_capital_usage = 0.90

        self.reserve_cash = 0.10

    def evaluate(self, portfolio):

        total = portfolio["portfolio_value"]

        invested = total - portfolio["cash"]

        invested_pct = invested / total

        available = total * self.max_capital_usage - invested

        return {

            "portfolio_value": total,

            "cash": portfolio["cash"],

            "invested": invested,

            "invested_pct": round(invested_pct * 100,2),

            "available_capital": max(0,available),

            "reserve_cash": total * self.reserve_cash

        }