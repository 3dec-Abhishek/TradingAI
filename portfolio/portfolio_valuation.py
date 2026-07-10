from portfolio.pnl_calculator import PnLCalculator




class PortfolioValuation:



    def __init__(self):


        self.pnl = PnLCalculator()





    def calculate(

        self,

        account,

        market_data

    ):


        positions = account.get_positions()



        total_position_value = 0


        total_pnl = 0



        position_details = {}



        for symbol, position in positions.items():



            if symbol not in market_data:


                continue



            current_price = market_data[symbol]



            result = self.pnl.calculate_position(

                position,

                current_price

            )



            position_details[symbol] = result



            total_position_value += result["current_value"]



            total_pnl += result["pnl"]





        cash = account.get_cash()



        portfolio_value = (

            cash +

            total_position_value

        )



        return {


            "cash":

            round(cash,2),



            "positions":

            position_details,



            "position_value":

            round(

                total_position_value,

                2

            ),



            "unrealized_pnl":

            round(

                total_pnl,

                2

            ),



            "portfolio_value":

            round(

                portfolio_value,

                2

            )

        }