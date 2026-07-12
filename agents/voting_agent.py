class VotingAgent:


    def analyze(
        self,
        signals,
        ai_response,
        regime
    ):


        votes = []


        strategy_signal = (
            signals.get(
                "signal",
                "HOLD"
            )
        )


        votes.append(
            strategy_signal
        )



        if isinstance(
            ai_response,
            dict
        ):


            votes.append(

                ai_response.get(
                    "action",
                    "HOLD"
                )

            )



        if regime.get(
            "regime"
        ) == "BULLISH":


            votes.append(
                "BUY"
            )



        buy = votes.count(
            "BUY"
        )


        sell = votes.count(
            "SELL"
        )



        if buy > sell:

            return "BUY"


        elif sell > buy:

            return "SELL"


        return "HOLD"