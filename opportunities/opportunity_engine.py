class OpportunityEngine:


    def __init__(self):

        self.name = "Opportunity Engine"



    def evaluate(
        self,
        market,
        signals,
        decision,
        risk,
        regime,
        ai_response=None
    ):

        score = 50

        reasons = []



        # =========================
        # Strategy
        # =========================

        action = signals.get(
            "signal",
            signals.get(
                "action",
                "HOLD"
            )
        )


        confidence = signals.get(
            "confidence",
            50
        )


        if action == "BUY":

            score += 15

            reasons.append(
                "Strategy generated BUY signal"
            )


        elif action == "SELL":

            score -= 15

            reasons.append(
                "Strategy generated SELL signal"
            )



        score += int(
            confidence * 0.2
        )



        # =========================
        # Regime
        # =========================

        market_regime = regime.get(
            "regime",
            "UNKNOWN"
        )


        if market_regime == "BULLISH":

            score += 15

            reasons.append(
                "Bullish market regime"
            )


        elif market_regime == "BEARISH":

            score -= 20

            reasons.append(
                "Bearish market regime"
            )


        elif market_regime == "HIGH_VOLATILITY":

            score -= 10

            reasons.append(
                "High volatility"
            )



        # =========================
        # Risk
        # =========================

        risk_status = risk.get(
            "status",
            "UNKNOWN"
        )


        if risk_status in [
            "PASS",
            "APPROVED"
        ]:

            score += 10

            reasons.append(
                "Risk approved"
            )


        elif risk_status in [
            "FAIL",
            "REJECTED"
        ]:

            score -= 30

            reasons.append(
                "Risk rejected"
            )



        # =========================
        # AI Agreement
        # =========================

        if isinstance(
            ai_response,
            dict
        ):

            ai_action = ai_response.get(
                "action",
                "HOLD"
            )


            if ai_action == action:

                score += 5

                reasons.append(
                    "AI agrees with strategy"
                )



        # =========================
        # Clamp Score
        # =========================

        score = max(
            0,
            min(
                100,
                score
            )
        )



        return {


            "symbol": market.get(
                "symbol",
                "UNKNOWN"
            ),


            "score": score,


            "action": decision.get(
                "action",
                "HOLD"
            ),


            "confidence": decision.get(
                "confidence",
                confidence
            ),


            "strategy": signals.get(
                "strategy",
                "UNKNOWN"
            ),


            "regime": market_regime,


            "reasons": reasons

        }