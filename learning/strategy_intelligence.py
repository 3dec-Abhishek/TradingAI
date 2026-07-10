class StrategyIntelligence:


    def __init__(self):

        self.performance = {}



    def record_strategy(

        self,

        strategy,

        success

    ):


        if strategy not in self.performance:


            self.performance[strategy] = {


                "trades": 0,

                "wins": 0

            }



        self.performance[strategy]["trades"] += 1



        if success:

            self.performance[strategy]["wins"] += 1




    def calculate_score(

        self,

        strategy

    ):


        data = self.performance.get(

            strategy

        )


        if not data:

            return 0



        trades = data["trades"]


        if trades == 0:

            return 0



        wins = data["wins"]



        return round(

            (

                wins /

                trades

            ) * 100,

            2

        )





    def rank_strategies(self):


        ranking = {}



        for strategy in self.performance:


            ranking[strategy] = self.calculate_score(

                strategy

            )



        return dict(

            sorted(

                ranking.items(),

                key=lambda item: item[1],

                reverse=True

            )

        )





    def best_strategy(self):


        ranking = self.rank_strategies()



        if not ranking:

            return None



        return list(

            ranking.keys()

        )[0]