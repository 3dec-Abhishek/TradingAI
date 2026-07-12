import numpy as np



class CorrelationEngine:


    def analyze(
        self,
        market_data
    ):


        if len(market_data) < 2:

            return {

                "correlation":

                0,

                "status":

                "LOW"

            }



        prices = []


        for item in market_data:

            prices.append(
                item.get(
                    "price",
                    0
                )
            )


        correlation = np.corrcoef(
            prices
        )[0][1]



        return {


            "correlation":

            round(
                float(correlation),
                2
            ),


            "status":

            "HIGH"

            if correlation > 0.8

            else

            "NORMAL"

        }