from learning.strategy_intelligence import StrategyIntelligence



class StrategyTracker:


    def __init__(self, tracker):


        self.performance_tracker = tracker


        self.intelligence = StrategyIntelligence()




    def record(

        self,

        strategy,

        trade_result

    ):


        if not strategy:

            strategy = "UNKNOWN"



        success = (

            trade_result.get(

                "status"

            )

            ==

            "FILLED"

        )



        self.intelligence.record_strategy(

            strategy,

            success

        )




    def get_rankings(self):


        return self.intelligence.rank_strategies()




    def get_best_strategy(self):


        return self.intelligence.best_strategy()