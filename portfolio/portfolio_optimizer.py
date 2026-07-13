class PortfolioOptimizer:

    def optimize(self, positions):

        if not positions:

            return []

        total = sum(p["market_value"] for p in positions)

        recommendations=[]

        for p in positions:

            weight = p["market_value"]/total

            recommendations.append({

                "symbol":p["symbol"],

                "weight":round(weight*100,2),

                "target_weight":10,

                "rebalance":

                    weight>0.15 or weight<0.05

            })

        return recommendations