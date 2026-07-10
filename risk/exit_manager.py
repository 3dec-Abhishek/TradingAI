class ExitManager:


    def __init__(self):


        self.stop_loss_percent = 5

        self.take_profit_percent = 10





    def calculate_levels(

        self,

        entry_price

    ):


        stop_loss = (

            entry_price *

            (

                1 -

                self.stop_loss_percent / 100

            )

        )



        take_profit = (

            entry_price *

            (

                1 +

                self.take_profit_percent / 100

            )

        )



        return {


            "entry":

            round(

                entry_price,

                2

            ),


            "stop_loss":

            round(

                stop_loss,

                2

            ),


            "take_profit":

            round(

                take_profit,

                2

            )

        }





    def evaluate(

        self,

        position,

        current_price

    ):



        entry = position.get(

            "average_price"

        )



        if not entry:


            return {


                "action":

                "HOLD",

                "reason":

                "No entry price"

            }



        levels = self.calculate_levels(

            entry

        )



        if current_price <= levels["stop_loss"]:


            return {


                "action":

                "SELL",


                "reason":

                "Stop loss triggered",


                "levels":

                levels

            }




        if current_price >= levels["take_profit"]:


            return {


                "action":

                "SELL",


                "reason":

                "Take profit triggered",


                "levels":

                levels

            }




        return {


            "action":

            "HOLD",


            "reason":

            "Exit levels not reached",


            "levels":

            levels

        }