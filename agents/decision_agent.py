from learning.confidence_adjuster import ConfidenceAdjuster



class DecisionAgent:


    def __init__(self):


        self.confidence_adjuster = ConfidenceAdjuster()




    def analyze(

        self,

        portfolio,

        market,

        signals,

        risk,

        ai_response,

        portfolio_health=None,

        history=None,

        best_strategy=None

    ):



        symbol = market.get(

            "symbol"

        )



        reasons = []



        # =========================
        # Risk Protection
        # =========================

        if risk.get(

            "trade_status"

        ) == "REJECTED":


            return {


                "symbol":

                symbol,


                "action":

                "HOLD",


                "confidence":

                90,


                "reason":

                [

                    "Risk rejected trade"

                ]

            }





        buy_votes = 0

        sell_votes = 0




        selected_strategy = None




        # =========================
        # Strategy Evaluation
        # =========================


        for signal in signals:


            name = signal.get(

                "strategy"

            )


            value = signal.get(

                "signal"

            )



            if (

                best_strategy

                and

                name == best_strategy

            ):

                selected_strategy = signal



            if value == "BUY":

                buy_votes += 1



            elif value == "SELL":

                sell_votes += 1





        if selected_strategy:


            reasons.append(

                "Best performing strategy: "

                +

                best_strategy

            )



            if selected_strategy.get(

                "signal"

            ) == "BUY":


                buy_votes += 1



            elif selected_strategy.get(

                "signal"

            ) == "SELL":


                sell_votes += 1






        # =========================
        # Final Action
        # =========================


        if buy_votes > sell_votes:


            action = "BUY"

            confidence = 65


            reasons.append(

                "Strategy voting favors BUY"

            )



        elif sell_votes > buy_votes:


            action = "SELL"

            confidence = 65


            reasons.append(

                "Strategy voting favors SELL"

            )



        else:


            action = "HOLD"

            confidence = 50


            reasons.append(

                "No strategy agreement"

            )






        # =========================
        # Learning Adjustment
        # =========================


        confidence = self.confidence_adjuster.adjust_confidence(

            action,

            confidence,

            history or []

        )



        reasons.append(

            "Confidence adjusted from historical performance"

        )




        return {


            "symbol":

            symbol,


            "action":

            action,


            "confidence":

            confidence,


            "reason":

            reasons

        }