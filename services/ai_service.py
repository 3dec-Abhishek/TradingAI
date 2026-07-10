from agents.ai_trading_agent import AITradingAgent



class AIService:


    def __init__(self):

        self.agent = AITradingAgent()



    def analyze(

        self,

        portfolio,

        market,

        signals

    ):


        return (

            self.agent
            .analyze(

                portfolio,

                market,

                signals

            )

        )