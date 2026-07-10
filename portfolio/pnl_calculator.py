class PnLCalculator:



    def calculate_position(

        self,

        position,

        current_price

    ):


        quantity = position["quantity"]


        avg_price = position["average_price"]



        invested = quantity * avg_price



        current_value = quantity * current_price



        pnl = current_value - invested



        pnl_percent = (

            pnl /

            invested

        ) * 100



        return {


            "quantity":

            quantity,


            "average_price":

            avg_price,


            "current_value":

            current_value,


            "pnl":

            round(pnl,2),


            "pnl_percent":

            round(pnl_percent,2)

        }