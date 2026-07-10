class ExitExecutor:


    def __init__(self, order_manager):


        self.order_manager = order_manager





    def execute_exit(

        self,

        exit_signal,

        symbol,

        price,

        quantity

    ):


        if exit_signal.get("action") != "SELL":


            return {


                "status":

                "NO_EXIT",


                "reason":

                exit_signal.get(

                    "reason"

                )

            }



        sell_order = {


            "symbol":

            symbol,


            "action":

            "SELL",


            "quantity":

            quantity,


            "price":

            price

        }



        result = self.order_manager.execute(

            sell_order,

            {

                "symbol":

                symbol,

                "price":

                price

            }

        )



        return {


            "status":

            "EXIT_EXECUTED",


            "trade":

            result,


            "reason":

            exit_signal.get(

                "reason"

            )

        }