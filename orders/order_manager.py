from broker.paper_broker import PaperBroker



class OrderManager:


    def __init__(self, broker):

        self.broker = broker



    def execute(

        self,

        decision,

        market

    ):


        action = decision.get(

            "action",

            "HOLD"

        )


        symbol = market.get(

            "symbol"

        )


        price = market.get(

            "price"

        )



        # =========================
        # No Trade
        # =========================

        if action == "HOLD":


            return {


                "status":

                "NO TRADE",


                "action":

                "HOLD",


                "symbol":

                symbol,


                "quantity":

                0,


                "price":

                price

            }



        # =========================
        # Create Order
        # =========================


        order = {


            "action":

            action,


            "symbol":

            symbol,


            "quantity":

            1,


            "price":

            price

        }



        result = self.broker.execute_order(

            order

        )



        return result