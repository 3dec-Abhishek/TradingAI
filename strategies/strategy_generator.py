class StrategyGenerator:



    def generate(self):


        strategies=[]


        strategies.append({

            "name":
            "Momentum_AI",

            "rules":
            {

            "buy":
            "price>sma20",

            "sell":
            "rsi>70"

            }

        })



        strategies.append({

            "name":
            "Mean_Reversion_AI",

            "rules":
            {

            "buy":
            "rsi<30",

            "sell":
            "rsi>60"

            }

        })


        return strategies