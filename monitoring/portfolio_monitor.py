class PortfolioMonitor:


    def __init__(self):

        self.max_position_percentage = 25

        self.minimum_cash_percentage = 10



    def analyze(

        self,

        portfolio

    ):


        alerts = []

        metrics = {}



        account = portfolio.get(

            "account",

            {}

        )



        positions = portfolio.get(

            "positions",

            []

        )



        portfolio_value = account.get(

            "portfolio_value",

            0

        )


        cash = account.get(

            "cash",

            0

        )



        if portfolio_value == 0:


            return {

                "status":"ERROR",

                "alerts":[

                    "Portfolio value unavailable"

                ]

            }



        # =========================
        # Cash Analysis
        # =========================


        cash_percentage = (

            cash /

            portfolio_value

        ) * 100



        metrics["cash_percentage"] = round(

            cash_percentage,

            2

        )



        if cash_percentage < self.minimum_cash_percentage:


            alerts.append(

                "Low cash reserve"

            )



        # =========================
        # Position Concentration
        # =========================


        for position in positions:


            value = position.get(

                "value",

                0

            )


            exposure = (

                value /

                portfolio_value

            ) * 100



            symbol = position.get(

                "symbol"

            )


            metrics[

                f"{symbol}_exposure"

            ] = round(

                exposure,

                2

            )



            if exposure > self.max_position_percentage:


                alerts.append(

                    f"{symbol} concentration exceeds limit"

                )



        # =========================
        # Final Status
        # =========================


        status = (

            "HEALTHY"

            if len(alerts) == 0

            else

            "WARNING"

        )



        return {


            "status": status,


            "metrics": metrics,


            "alerts": alerts


        }