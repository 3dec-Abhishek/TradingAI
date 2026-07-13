class RebalanceEngine:

    def rebalance(

        self,

        optimizer,

        capital

    ):

        trades=[]

        for stock in optimizer:

            if stock["rebalance"]:

                trades.append({

                    "symbol":stock["symbol"],

                    "action":"REBALANCE"

                })

        return trades