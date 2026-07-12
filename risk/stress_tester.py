class StressTester:



    def run(
        self,
        portfolio_value
    ):


        scenarios = {


            "market_crash":

            portfolio_value * 0.7,


            "bear_market":

            portfolio_value * 0.85,


            "normal_drop":

            portfolio_value * 0.95

        }



        return {


            "scenarios":

            scenarios,


            "worst_case":

            min(
                scenarios.values()
            )

        }