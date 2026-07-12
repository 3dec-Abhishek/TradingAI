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


        strategy = "UNKNOWN"

        strategy_action = "HOLD"



        # ==================================================
        # NORMALIZE SIGNALS
        # ==================================================

        if isinstance(signals, list):


            normalized = {}


            buy_votes = 0

            sell_votes = 0



            for signal in signals:


                if not isinstance(
                    signal,
                    dict
                ):

                    continue



                strategy = signal.get(
                    "strategy",
                    strategy
                )


                action = signal.get(
                    "signal",
                    signal.get(
                        "action",
                        "HOLD"
                    )
                )


                conf = signal.get(
                    "confidence",
                    50
                )


                confidence += int(
                    conf * 0.20
                )



                if action == "BUY":

                    buy_votes += 1



                elif action == "SELL":

                    sell_votes += 1




            if buy_votes > sell_votes:

                strategy_action = "BUY"



            elif sell_votes > buy_votes:

                strategy_action = "SELL"



            else:

                strategy_action = "HOLD"




        elif isinstance(
            signals,
            dict
        ):


            strategy = signals.get(
                "strategy",
                "UNKNOWN"
            )


            strategy_action = signals.get(
                "signal",
                signals.get(
                    "action",
                    "HOLD"
                )
            )


            confidence += int(

                signals.get(
                    "confidence",
                    50
                )
                *
                0.20

            )



        else:


            strategy_action = "HOLD"

            reasons.append(
                "No valid strategy signal"
            )



        # ==================================================
        # PHASE 18.7 AI VOTE
        # ==================================================

        final_vote = "HOLD"


        if isinstance(
            signals,
            dict
        ):


            final_vote = signals.get(

                "final_vote",

                "HOLD"

            )



        if final_vote != "HOLD":


            strategy_action = final_vote


            confidence += 10


            reasons.append(

                f"AI voting system selected {final_vote}"

            )



        # ==================================================
        # STRATEGY CONFIDENCE
        # ==================================================


        if strategy_action == "BUY":


            confidence += 15


            reasons.append(
                "Strategy favors BUY"
            )



        elif strategy_action == "SELL":


            confidence += 10


            reasons.append(
                "Strategy favors SELL"
            )



        else:


            confidence -= 5


            reasons.append(
                "No strong strategy signal"
            )



        # ==================================================
        # RISK ANALYSIS
        # ==================================================

        if not isinstance(
            risk,
            dict
        ):

            risk = {}



        risk_status = str(

            risk.get(
                "status",
                ""
            )

        ).upper()



        if risk_status in [

            "FAIL",

            "FAILED",

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



        # ==================================================
        # AI RESPONSE
        # ==================================================

        if isinstance(
            ai_response,
            dict
        ):


            ai_action = ai_response.get(

                "action",

                "HOLD"

            )



            if ai_action == strategy_action:


                confidence += 5


                reasons.append(

                    "AI agrees with strategy"

                )



        # ==================================================
        # MARKET REGIME
        # ==================================================

        market_regime = "UNKNOWN"



        if isinstance(
            regime,
            dict
        ):


            market_regime = regime.get(

                "regime",

                "UNKNOWN"

            )



            if market_regime == "BULLISH":


                confidence += 10


                reasons.append(

                    "Bullish market regime"

                )



            elif market_regime == "BEARISH":


                confidence -= 20


                reasons.append(

                    "Bearish market regime"

                )



            elif market_regime == "HIGH_VOLATILITY":


                confidence -= 15


                reasons.append(

                    "High volatility"

                )



            elif market_regime == "SIDEWAYS":


                confidence -= 5


                reasons.append(

                    "Sideways market"

                )



        # ==================================================
        # CONFIDENCE LIMIT
        # ==================================================

        confidence = max(

            0,

            min(

                100,

                confidence

            )

        )



        # ==================================================
        # FINAL ACTION
        # ==================================================

        if confidence < 60:


            action = "HOLD"


            reasons.append(

                "Confidence below trading threshold"

            )



        else:


            action = strategy_action



        # ==================================================
        # RETURN DECISION
        # ==================================================

        return {


            "symbol":

            symbol,



            "action":

            action,



            "strategy":

            strategy,



            "confidence":

            confidence,



            "regime":

            market_regime,



            "reasons":

            reasons,


            # backward compatibility

            "reason":

            reasons

        }