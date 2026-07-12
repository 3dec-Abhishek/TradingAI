import numpy as np



class MonteCarloRisk:


    def simulate(
        self,
        price,
        volatility,
        days=30,
        simulations=1000
    ):


        results=[]


        for i in range(simulations):


            future = price * np.exp(

                np.random.normal(

                    0,

                    volatility,

                    days

                ).sum()

            )


            results.append(
                future
            )



        return {


            "average":

            np.mean(results),


            "worst_case":

            np.percentile(
                results,
                5
            ),


            "best_case":

            np.percentile(
                results,
                95
            )

        }