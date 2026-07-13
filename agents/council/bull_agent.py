class BullAgent:


    def analyze(
        self,
        market,
        signals
    ):


        confidence = 50

        reasons = []


        if market.get(
            "trend"
        ) == "BULLISH":

            confidence += 25

            reasons.append(
                "Positive market trend"
            )


        if signals.get(
            "signal"
        ) == "BUY":

            confidence += 20

            reasons.append(
                "Strategy supports buying"
            )


        return {

            "agent":
            "BULL",

            "vote":
            "BUY"
            if confidence >=70
            else "HOLD",

            "confidence":
            confidence,

            "reasons":
            reasons

        }