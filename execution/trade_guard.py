class TradeGuard:


    def validate(
        self,
        decision,
        risk,
        portfolio
    ):


        errors=[]


        if decision["action"] not in [
            "BUY",
            "SELL",
            "HOLD"
        ]:

            errors.append(
                "Invalid action"
            )


        if decision["confidence"] < 60:

            errors.append(
                "Confidence too low"
            )


        if risk.get("status") == "FAIL":

            errors.append(
                "Risk rejected"
            )


        if len(errors):

            return {

                "approved":False,

                "errors":errors

            }


        return {

            "approved":True,

            "errors":[]

        }