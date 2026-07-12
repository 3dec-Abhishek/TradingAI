class ExposureAnalyzer:


    def analyze(
        self,
        portfolio
    ):


        positions = portfolio.get(
            "positions",
            []
        )


        total = portfolio.get(
            "portfolio_value",
            0
        )


        exposure = {}



        for position in positions:


            symbol = position.get(
                "symbol",
                "UNKNOWN"
            )


            value = position.get(
                "value",
                0
            )


            exposure[symbol] = round(

                value /

                total *

                100,

                2

            )



        return {


            "exposure":

            exposure,


            "status":

            "CHECKED"

        }