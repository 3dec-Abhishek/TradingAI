class DynamicRiskEngine:



    def __init__(self):


        self.max_position_percent = 10

        self.max_portfolio_risk = 20

        self.max_daily_loss_percent = 2





    def analyze(

        self,

        valuation,

        proposed_trade

    ):



        portfolio_value = valuation.get(

            "portfolio_value",

            0

        )



        cash = valuation.get(

            "cash",

            0

        )



        position_value = valuation.get(

            "position_value",

            0

        )



        if portfolio_value == 0:


            return {


                "status":

                "REJECTED",


                "reason":

                "Invalid portfolio value"

            }




        trade_size = proposed_trade.get(

            "trade_size",

            0

        )



        options_value = proposed_trade.get(

            "options_value",

            0

        )



        daily_loss = proposed_trade.get(

            "today_loss",

            0

        )



        # =========================
        # Exposure Calculation
        # =========================


        current_exposure = (

            position_value /

            portfolio_value

        ) * 100



        new_position_exposure = (

            (

                position_value +

                trade_size

            )

            /

            portfolio_value

        ) * 100




        daily_loss_percent = (

            daily_loss /

            portfolio_value

        ) * 100




        checks = {



            "current_exposure":{


                "value":

                round(

                    current_exposure,

                    2

                ),


                "limit":

                self.max_portfolio_risk

            },



            "new_position_exposure":{


                "value":

                round(

                    new_position_exposure,

                    2

                ),


                "limit":

                self.max_position_percent

            },



            "daily_loss":{


                "value":

                round(

                    daily_loss_percent,

                    2

                ),


                "limit":

                self.max_daily_loss_percent

            }

        }




        failed = []



        for name, data in checks.items():


            if data["value"] > data["limit"]:


                failed.append(name)




        return {


            "checks":

            checks,


            "available_cash":

            round(

                cash,

                2

            ),



            "status":

            "APPROVED"

            if not failed

            else

            "REJECTED",



            "failed":

            failed

        }