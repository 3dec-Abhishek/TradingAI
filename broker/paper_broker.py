class PaperBroker:


    def __init__(self):

        self.account = {

            "cash": 5000,

            "portfolio_value": 25000

        }


        self.positions = [

            {
                "symbol": "AAPL",
                "quantity": 20,
                "average_price": 280,
                "current_price": 313.39
            },

            {
                "symbol": "TSLA",
                "quantity": 5,
                "average_price": 600,
                "current_price": 300
            }

        ]



    def get_account(self):

        return self.account



    def get_positions(self):


        positions = []


        for position in self.positions:


            value = (
                position["quantity"]
                *
                position["current_price"]
            )


            gain_percent = (

                (
                    position["current_price"]
                    -
                    position["average_price"]
                )
                /
                position["average_price"]

            ) * 100



            positions.append(

                {

                    "symbol":
                    position["symbol"],


                    "quantity":
                    position["quantity"],


                    "value":
                    round(value,2),


                    "gain_percent":
                    round(gain_percent,2)

                }

            )


        return positions



    def buy(
        self,
        symbol,
        quantity,
        price
    ):


        cost = quantity * price


        if cost > self.account["cash"]:

            return {

                "status":"REJECTED",

                "reason":
                "Insufficient cash"

            }



        self.account["cash"] -= cost



        self.positions.append(

            {

                "symbol":symbol,

                "quantity":quantity,

                "average_price":price,

                "current_price":price

            }

        )


        return {


            "status":
            "FILLED",


            "action":
            "BUY",


            "symbol":
            symbol,


            "quantity":
            quantity,


            "price":
            price

        }




    def sell(
        self,
        symbol,
        quantity,
        price
    ):


        for position in self.positions:


            if position["symbol"] == symbol:


                if position["quantity"] >= quantity:


                    position["quantity"] -= quantity


                    self.account["cash"] += (
                        quantity * price
                    )


                    return {

                        "status":
                        "FILLED",

                        "action":
                        "SELL",

                        "symbol":
                        symbol,

                        "quantity":
                        quantity,

                        "price":
                        price

                    }



        return {

            "status":
            "REJECTED",

            "reason":
            "Position not found"

        }