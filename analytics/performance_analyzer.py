class PerformanceAnalyzer:


    def __init__(self):

        self.trades = []



    def add_trade(self, trade):

        self.trades.append(trade)



    def analyze(self):


        if not self.trades:


            return {


                "total_trades": 0,

                "wins": 0,

                "losses": 0,

                "win_rate": 0,

                "profit_factor": 0,

                "average_return": 0,

                "max_drawdown": 0


            }



        wins = 0

        losses = 0

        profits = []

        losses_amount = []



        for trade in self.trades:


            pnl = trade.get(

                "pnl",

                0

            )



            if pnl > 0:


                wins += 1

                profits.append(pnl)



            elif pnl < 0:


                losses += 1

                losses_amount.append(

                    abs(pnl)

                )



        total = len(self.trades)



        win_rate = (

            wins / total

        ) * 100



        gross_profit = sum(

            profits

        )



        gross_loss = sum(

            losses_amount

        )



        profit_factor = (

            gross_profit / gross_loss

            if gross_loss > 0

            else gross_profit

        )



        average_return = sum(

            [

                t.get("pnl",0)

                for t in self.trades

            ]

        ) / total



        return {


            "total_trades": total,


            "wins": wins,


            "losses": losses,


            "win_rate": round(

                win_rate,

                2

            ),


            "profit_factor": round(

                profit_factor,

                2

            ),


            "average_return": round(

                average_return,

                2

            )


        }