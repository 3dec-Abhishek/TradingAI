class StrategyOptimizer:


    def __init__(self):

        self.strategies = {}



    def record(

        self,

        strategy,

        trade

    ):


        if strategy not in self.strategies:


            self.strategies[strategy] = {

                "trades": 0,

                "wins": 0,

                "losses": 0,

                "profit": 0

            }



        data = self.strategies[strategy]


        data["trades"] += 1



        pnl = trade.get(

            "pnl",

            0

        )



        data["profit"] += pnl



        if pnl > 0:

            data["wins"] += 1


        elif pnl < 0:

            data["losses"] += 1





    def analyze(self):


        results = {}



        for name, data in self.strategies.items():


            trades = data["trades"]


            win_rate = (

                data["wins"] /

                trades *

                100

                if trades

                else 0

            )



            score = (

                win_rate * 0.6

                +

                data["profit"] * 0.4

            )



            results[name] = {


                "trades": trades,


                "win_rate": round(

                    win_rate,

                    2

                ),


                "profit": round(

                    data["profit"],

                    2

                ),


                "score": round(

                    score,

                    2

                )

            }



        return results





    def get_best_strategy(self):


        results = self.analyze()



        if not results:

            return None



        return max(

            results,

            key=lambda x:

            results[x]["score"]

        )
    
    # Backwards compatibility for the previous method name
    def best_strategy_name(self):
        return self.get_best_strategy()