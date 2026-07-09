class DecisionAgent:


    def analyze(
        self,
        portfolio,
        market,
        signals,
        risk,
        ai_analysis
    ):


        decision = {

            "symbol": market["symbol"],

            "action": "HOLD",

            "confidence": 0,

            "reason": []

        }


        # Risk first

        if not risk["approved"]:

            decision["action"] = "NO TRADE"

            decision["confidence"] = 100

            decision["reason"].append(
                "Risk rules rejected trade"
            )

            return decision



        # Strategy evaluation

        buy_score = 0
        sell_score = 0



        for signal in signals:


            if signal["signal"] == "BUY":

                buy_score += signal["confidence"]


            elif signal["signal"] == "SELL":

                sell_score += signal["confidence"]



        if buy_score > sell_score:

            decision["action"] = "BUY"

            decision["confidence"] = buy_score



        elif sell_score > buy_score:

            decision["action"] = "SELL"

            decision["confidence"] = sell_score



        else:

            decision["action"] = "HOLD"

            decision["confidence"] = 50



        decision["reason"].append(
            "Decision generated from strategy + risk + AI analysis"
        )


        return decision