class PositionSizer:


    def __init__(self):


        self.risk_percent = 2



    def calculate(

        self,

        portfolio_value,

        price,

        confidence,

        volatility=1

    ):


        if portfolio_value <= 0:


            return {


                "quantity":0,

                "reason":"Invalid portfolio"

            }




        # Money allowed to risk

        risk_amount = (

            portfolio_value *

            self.risk_percent /

            100

        )



        # Adjust by confidence


        confidence_multiplier = (

            confidence /

            100

        )



        adjusted_risk = (

            risk_amount *

            confidence_multiplier

        )



        # Adjust by volatility


        adjusted_risk = (

            adjusted_risk /

            volatility

        )



        quantity = int(

            adjusted_risk /

            price

        )



        if quantity < 1:

            quantity = 1



        return {


            "quantity":

            quantity,


            "risk_amount":

            round(

                adjusted_risk,

                2

            ),


            "confidence":

            confidence,


            "volatility":

            volatility

        }