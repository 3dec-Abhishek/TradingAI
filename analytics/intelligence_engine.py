class IntelligenceEngine:


    def analyze(
        self,
        trades
    ):


        wins=[]

        losses=[]


        for trade in trades:


            pnl=trade.get(
                "pnl",
                0
            )


            if pnl>0:

                wins.append(
                    pnl
                )

            else:

                losses.append(
                    pnl
                )



        return {


            "win_rate":

            (
                len(wins)
                /
                len(trades)
                *
                100
            )
            if trades else 0,


            "average_win":

            sum(wins)/len(wins)
            if wins else 0,


            "average_loss":

            sum(losses)/len(losses)
            if losses else 0,


            "total_trades":

            len(trades)


        }