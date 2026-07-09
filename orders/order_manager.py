class OrderManager:


    def __init__(self, broker):

        self.broker = broker



    def execute(self, decision, market):


        symbol = decision["symbol"]

        action = decision["action"]


        price = market["price"]



        if action == "BUY":


            return self.broker.buy(

                symbol,

                1,

                price

            )



        elif action == "SELL":


            return self.broker.sell(

                symbol,

                1,

                price

            )



        else:


            return {

                "status":"NO ACTION",

                "reason":"AI decided HOLD"

            }