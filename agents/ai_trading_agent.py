from llm.local_llm import LocalLLM



class AITradingAgent:


    def __init__(self):

        self.llm = LocalLLM()



    def analyze(
            self,
            portfolio,
            market,
            strategies
        ):


        prompt = f"""

Portfolio:

{portfolio}


Market:

{market}


Strategies:

{strategies}



Analyze this trading situation.

Provide:

1. Market condition
2. Risk level
3. Strategy evaluation
4. Possible action
5. Explanation

"""


        return self.llm.ask(prompt)
