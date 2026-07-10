class DecisionAgent:


    def __init__(self):

        pass



    def analyze(
        self,
        portfolio,
        market,
        signals,
        risk,
        ai_response,
        regime=None
    ):


        symbol = market.get(
            "symbol",
            "UNKNOWN"
        )


        confidence = 50


        reasons = []



        # =========================
        # Strategy Analysis
        # =========================


        strategy_action = "HOLD"


        if isinstance(signals, list):


            buy_votes = 0

            sell_votes = 0


            for signal in signals:


                action = signal.get(

                    "signal",

                    signal.get(

                        "action",

                        "HOLD"

                    )

                )


                if action == "BUY":

                    buy_votes += 1


                elif action == "SELL":

                    sell_votes += 1



            if buy_votes > sell_votes:

                strategy_action = "BUY"


            elif sell_votes > buy_votes:

                strategy_action = "SELL"



        elif isinstance(signals, dict):


            strategy_action = signals.get(

                "action",

                signals.get(

                    "signal",

                    "HOLD"

                )

            )



        # =========================
        # Base Confidence
        # =========================


        if strategy_action == "BUY":


            confidence += 25

            reasons.append(

                "Strategy signals support BUY"

            )



        elif strategy_action == "SELL":


            confidence += 25

            reasons.append(

                "Strategy signals support SELL"

            )


        else:


            reasons.append(

                "No strong strategy signal"

            )



        # =========================
        # Risk Evaluation
        # =========================


        risk_status = risk.get(

            "status",

            "UNKNOWN"

        )


        if risk_status in [

            "FAIL",

            "REJECTED"

        ]:


            confidence -= 40


            reasons.append(

                "Risk rejected trade"

            )



        elif risk_status in [

            "PASS",

            "APPROVED"

        ]:


            confidence += 10


            reasons.append(

                "Risk approved"

            )



        # =========================
        # Market Regime
        # =========================


        if regime:


            current_regime = regime.get(

                "regime",

                "UNKNOWN"

            )


            if current_regime == "BULLISH":


                confidence += 10


                reasons.append(

                    "Bullish market regime"

                )



            elif current_regime == "BEARISH":


                confidence -= 20


                reasons.append(

                    "Bearish market regime"

                )



            elif current_regime == "HIGH_VOLATILITY":


                confidence -= 15


                reasons.append(

                    "High volatility detected"

                )



            elif current_regime == "SIDEWAYS":


                confidence -= 5


                reasons.append(

                    "Sideways market"

                )



        # =========================
        # AI Recommendation
        # =========================


        if isinstance(ai_response, dict):


            ai_action = ai_response.get(

                "action",

                "HOLD"

            )


            if ai_action == strategy_action:


                confidence += 5


                reasons.append(

                    "AI agrees with strategy"

                )



        # =========================
        # Clamp Confidence
        # =========================


        confidence = max(

            0,

            min(

                confidence,

                100

            )

        )



        # =========================
        # Final Decision
        # =========================


        action = "HOLD"



        if confidence >= 60:


            if strategy_action == "BUY":

                action = "BUY"


            elif strategy_action == "SELL":

                action = "SELL"



        # =========================
        # Final Object
        # =========================


        return {


            "symbol": symbol,


            "action": action,


            "confidence": confidence,


            "strategy": self.extract_strategy(

                signals

            ),


            "regime": (

                regime.get("regime")

                if regime

                else "UNKNOWN"

            ),


            "reason": reasons


        }




    def extract_strategy(self, signals):


        if isinstance(signals, dict):

            return signals.get(

                "strategy",

                "UNKNOWN"

            )


        if isinstance(signals, list) and len(signals) > 0:


            return signals[0].get(

                "strategy",

                "UNKNOWN"

            )


        return "UNKNOWN"