class DecisionAgent:



    def analyze(

        self,

        portfolio,

        market,

        signals,

        risk,

        ai_response,

        portfolio_health=None

    ):



        # =========================
        # Portfolio Safety Check
        # =========================


        if portfolio_health:


            if portfolio_health.get(

                "status"

            ) == "WARNING":



                return {


                    "symbol":

                    market["symbol"],



                    "action":

                    "HOLD",



                    "confidence":

                    80,



                    "reason":[

                        "Portfolio risk warning",

                        portfolio_health.get(

                            "alerts",

                            []

                        )

                    ]

                }




        # =========================
        # Risk Check
        # =========================


        if risk.get(

            "trade_status"

        ) != "APPROVED":



            return {


                "symbol":

                market["symbol"],



                "action":

                "HOLD",



                "confidence":

                90,



                "reason":[

                    "Risk rejected trade"

                ]

            }




        # =========================
        # Strategy Signals
        # =========================


        buy_score = 0

        sell_score = 0




        for signal in signals:


            if signal["signal"] == "BUY":


                buy_score += signal.get(

                    "confidence",

                    0

                )



            elif signal["signal"] == "SELL":


                sell_score += signal.get(

                    "confidence",

                    0

                )




        # =========================
        # Decision Logic
        # =========================


        if buy_score > sell_score:



            action = "BUY"


            confidence = buy_score




        elif sell_score > buy_score:



            action = "SELL"


            confidence = sell_score




        else:


            action = "HOLD"


            confidence = 50




        return {



            "symbol":

            market["symbol"],



            "action":

            action,



            "confidence":

            min(

                confidence,

                100

            ),



            "reason":[


                "Decision generated from strategy + risk + AI analysis"


            ]

        }