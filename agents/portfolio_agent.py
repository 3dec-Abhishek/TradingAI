from database.position_repository import PositionRepository



class PortfolioAgent:


    def __init__(

        self,

        broker=None

    ):

        self.broker = broker

        self.position_repository = PositionRepository()



    def analyze(self):


        # =========================
        # Account Information
        # =========================

        if self.broker:


            account = self.broker.get_account()


        else:

            account = {

                "cash": 0,

                "portfolio_value": 0

            }



        # =========================
        # Load Positions
        # =========================

        database_positions = (

            self.position_repository
            .get_positions()

        )



        positions = []



        total_position_value = 0



        for position in database_positions:


            symbol = position[0]

            quantity = position[1]

            average_price = position[2]



            value = (

                quantity *

                average_price

            )



            total_position_value += value



            positions.append(

                {

                    "symbol": symbol,

                    "quantity": quantity,

                    "value": round(
                        value,
                        2
                    ),

                    "average_price": round(
                        average_price,
                        2
                    )

                }

            )



        # =========================
        # Portfolio Value
        # =========================


        portfolio_value = (

            account.get(

                "cash",

                0

            )

            +

            total_position_value

        )



        account["portfolio_value"] = (

            portfolio_value

        )



        # =========================
        # Largest Position
        # =========================


        largest_position = None



        if positions:


            largest_position = max(

                positions,

                key=lambda x:x["value"]

            )["symbol"]



        # =========================
        # Result
        # =========================


        return {


            "account": account,


            "positions": positions,


            "largest_position": largest_position,


            "risk": "MEDIUM"

        }