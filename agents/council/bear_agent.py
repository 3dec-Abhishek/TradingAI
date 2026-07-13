class BearAgent:


    def analyze(
        self,
        market,
        signals
    ):


        confidence = 50

        reasons = []



        if market.get(
            "volatility",
            0
        ) > 0.3:


            confidence += 20

            reasons.append(
                "High volatility detected"
            )


        if market.get(
            "trend"
        ) == "BEARISH":


            confidence += 25

            reasons.append(
                "Negative trend"
            )


        return {


            "agent":

            "BEAR",


            "vote":

            "SELL"

            if confidence >=70

            else

            "HOLD",


            "confidence":

            confidence,


            "reasons":

            reasons

        }