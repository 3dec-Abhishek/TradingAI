from portfolio.portfolio_account import PortfolioAccount



class OrderManager:



    def __init__(

        self,

        broker

    ):


        self.broker = broker


        self.account = PortfolioAccount()





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
        # HOLD
        # =========================


        if action == "HOLD":


            return {


                "status":

                "NO TRADE",


                "action":

                "HOLD",


                "symbol":

                symbol

            }




        quantity = 1




        # =========================
        # BUY
        # =========================


        if action == "BUY":


            broker_result = self.broker.buy(

                symbol,

                quantity,

                price

            )



            self.account.buy(

                symbol,

                quantity,

                price

            )



        # =========================
        # SELL
        # =========================


        elif action == "SELL":


            broker_result = self.broker.sell(

                symbol,

                quantity,

                price

            )



            self.account.sell(

                symbol,

                quantity,

                price

            )



        else:


            return {


                "status":

                "INVALID ACTION"

            }




        return {


            "status":

            "FILLED",


            "action":

            action,


            "symbol":

            symbol,


            "quantity":

            quantity,


            "price":

            price,


            "portfolio":

            {


                "cash":

                self.account.get_cash(),


                "positions":

                self.account.get_positions()

            }

        }