class AnalystAgent:



    def analyze(
        self,
        market,
        research
    ):


        score = 50


        reasons = []



        if research:


            score = research.get(
                "research_score",
                50
            )


        if score >70:


            action="BUY"

            reasons.append(
                "Strong research"
            )


        elif score <40:


            action="SELL"

            reasons.append(
                "Weak research"
            )


        else:


            action="HOLD"



        return {


            "agent":

            "ANALYST",


            "vote":

            action,


            "confidence":

            score,


            "reasons":

            reasons

        }