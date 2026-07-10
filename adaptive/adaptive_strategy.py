class AdaptiveStrategyEngine:


    def __init__(self):

        self.weights = {

            "RSI": 1.0,

            "Moving Average": 1.0,

            "UNKNOWN": 1.0

        }



    def update_weights(self, strategy_results):


        for strategy, data in strategy_results.items():


            score = data.get(

                "score",

                0

            )


            if score > 50:


                self.weights[strategy] = min(

                    self.weights.get(strategy, 1.0) + 0.1,

                    2.0

                )


            else:


                self.weights[strategy] = max(

                    self.weights.get(strategy, 1.0) - 0.1,

                    0.5

                )



        return self.weights




    def adjust_confidence(

        self,

        strategy,

        confidence

    ):


        multiplier = self.weights.get(

            strategy,

            1.0

        )


        adjusted = confidence * multiplier


        return min(

            round(adjusted, 2),

            100

        )