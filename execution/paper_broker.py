class PaperBroker:


    def __init__(self):

        self.cash = 5000

        self.positions = []

        self.orders = []



    def place_order(self, trade):


        cost = (
            trade["premium"]
            *
            trade["contracts"]
            *
            100
        )


        if cost > self.cash:

            return {

                "status":"REJECTED",

                "reason":"Insufficient funds"

            }



        self.cash -= cost


        order = {

            "symbol": trade["symbol"],

            "type": trade["type"],

            "strike": trade["strike"],

            "expiration": trade["expiration"],

            "contracts": trade["contracts"],

            "entry_cost": cost

        }


        self.positions.append(order)

        self.orders.append(order)



        return {

            "status":"FILLED",

            "order":order,

            "remaining_cash":self.cash

        }



    def get_positions(self):

        return self.positions