class RiskJudge:



    def analyze(
        self,
        risk
    ):


        score = risk.get(
            "risk_score",
            50
        )


        if score <50:


            return {


                "agent":

                "RISK",


                "vote":

                "HOLD",


                "confidence":

                90,


                "reasons":

                [
                "Portfolio risk too high"
                ]

            }



        return {


            "agent":

            "RISK",


            "vote":

            "BUY",


            "confidence":

            score,


            "reasons":

            [
            "Risk acceptable"
            ]

        }