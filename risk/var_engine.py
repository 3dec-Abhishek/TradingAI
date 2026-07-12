class VaREngine:



    def calculate(
        self,
        portfolio_value,
        volatility
    ):


        confidence = 1.65


        var = (

            portfolio_value

            *

            volatility

            *

            confidence

        )



        return {


            "var":

            round(
                var,
                2
            ),


            "risk_level":

            "HIGH"

            if var >

            portfolio_value * 0.05

            else

            "NORMAL"

        }