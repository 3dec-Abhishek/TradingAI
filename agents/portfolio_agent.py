class PortfolioAgent:


    def __init__(self, broker):

        self.broker = broker



    def analyze(self):

        account = self.broker.get_account()

        positions = self.broker.get_positions()


        total = account["portfolio_value"]


        analysis = {

            "account": account,

            "positions": positions,

            "largest_position": None,

            "risk": "LOW"

        }


        largest = max(
            positions,
            key=lambda x: x["value"]
        )


        analysis["largest_position"] = largest["symbol"]


        exposure = (
            largest["value"] / total
        ) * 100


        if exposure > 20:
            analysis["risk"] = "HIGH"

        elif exposure > 10:
            analysis["risk"] = "MEDIUM"


        return analysis
