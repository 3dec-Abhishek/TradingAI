class TradeDecisionAgent:


    def analyze(
        self,
        market,
        signals,
        risk,
        options
    ):


        decision = {

            "action": "HOLD",

            "reason": "",

            "trade": None

        }


        # Risk must approve first

        if not risk.get("approved"):

            decision["reason"] = (
                "Risk rejected trade"
            )

            return decision



        # Options opportunity

        if options.get("strategy") != "NO OPTIONS TRADE":


            decision["action"] = "BUY"


            decision["reason"] = (
                "Options strategy approved"
            )


            decision["trade"] = options



        else:


            decision["reason"] = (
                "No valid options setup"
            )


        return decision