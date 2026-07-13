from agents.council.bull_agent import BullAgent
from agents.council.bear_agent import BearAgent
from agents.council.analyst_agent import AnalystAgent
from agents.council.risk_judge import RiskJudge



class CouncilEngine:



    def __init__(self):

        self.bull = BullAgent()

        self.bear = BearAgent()

        self.analyst = AnalystAgent()

        self.risk = RiskJudge()



    def decide(
        self,
        market,
        signals,
        research,
        risk
    ):


        votes = []


        votes.append(
            self.bull.analyze(
                market,
                signals
            )
        )


        votes.append(
            self.bear.analyze(
                market,
                signals
            )
        )


        votes.append(
            self.analyst.analyze(
                market,
                research
            )
        )


        votes.append(
            self.risk.analyze(
                risk
            )
        )



        buy = 0

        sell = 0

        hold = 0



        for vote in votes:


            if vote["vote"]=="BUY":

                buy+=1


            elif vote["vote"]=="SELL":

                sell+=1


            else:

                hold+=1



        if buy > sell and buy > hold:

            final="BUY"


        elif sell > buy and sell > hold:

            final="SELL"


        else:

            final="HOLD"



        confidence = sum(

            v["confidence"]

            for v in votes

        ) / len(votes)



        return {


            "decision":

            final,


            "confidence":

            round(
                confidence,
                2
            ),


            "votes":

            votes

        }