class RiskController:



    def evaluate(
        self,
        risk_score
    ):


        if risk_score < 40:


            return {


                "status":

                "HALT",


                "message":

                "Emergency risk shutdown"

            }



        return {


            "status":

            "ALLOW",


            "message":

            "Trading permitted"

        }