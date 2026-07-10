class PortfolioAccount:


    def __init__(self, starting_cash=5000):


        self.cash = starting_cash


        self.positions = {}




    def buy(

        self,

        symbol,

        quantity,

        price

    ):


        cost = quantity * price


        self.cash -= cost



        if symbol not in self.positions:


            self.positions[symbol] = {


                "quantity": quantity,


                "average_price": price

            }


        else:


            old = self.positions[symbol]


            total_quantity = (

                old["quantity"]

                +

                quantity

            )



            total_cost = (

                old["quantity"]

                *

                old["average_price"]

                +

                cost

            )



            old["quantity"] = total_quantity



            old["average_price"] = (

                total_cost /

                total_quantity

            )




    def sell(

        self,

        symbol,

        quantity,

        price

    ):


        if symbol not in self.positions:

            return False



        position = self.positions[symbol]



        if position["quantity"] < quantity:

            return False



        self.cash += quantity * price



        position["quantity"] -= quantity



        if position["quantity"] == 0:


            del self.positions[symbol]



        return True





    def get_positions(self):


        return self.positions





    def get_cash(self):


        return self.cash