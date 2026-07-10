class DatabaseAnalyzer:


    def __init__(self, database):

        self.database = database



    def analyze(self):


        trades = self.database.get_trades()



        total = len(trades)


        if total == 0:


            return {


                "total_trades": 0,


                "winning_trades": 0,


                "losing_trades": 0,


                "win_rate": 0,


                "buy_trades": 0,


                "sell_trades": 0

            }




        wins = sum(

            1

            for trade in trades

            if trade.get("success")

        )



        losses = total - wins



        buys = sum(

            1

            for trade in trades

            if trade.get("action") == "BUY"

        )



        sells = sum(

            1

            for trade in trades

            if trade.get("action") == "SELL"

        )




        return {


            "total_trades":

            total,


            "winning_trades":

            wins,


            "losing_trades":

            losses,


            "win_rate":

            round(

                wins / total * 100,

                2

            ),


            "buy_trades":

            buys,


            "sell_trades":

            sells

        }