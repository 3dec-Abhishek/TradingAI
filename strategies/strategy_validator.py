class StrategyValidator:



    def validate(
        self,
        strategy,
        backtest
    ):


        if backtest["return"] > 5:


            return {


                "approved":

                True,


                "strategy":

                strategy["name"]

            }


        return {


            "approved":

            False,


            "strategy":

            strategy["name"]

        }