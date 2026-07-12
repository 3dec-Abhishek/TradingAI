from options.greeks_engine import GreeksEngine

class OptionsAnalyzer:

    def __init__(self):
        self.greeks = GreeksEngine()

    def analyze(
        self,
        chain,
        market,
        signals
    ):


        result = {

            "symbol": market["symbol"],

            "strategy": "NONE",

            "contracts": [],

            "risk": 0,

            "reward": 0

        }



        bullish = False


        for signal in signals:


            if signal["signal"] == "BUY":

                bullish = True



        if bullish:


            calls = [

                x for x in chain

                if x["type"] == "CALL"

            ]



            result["strategy"] = (
                "Bull Call Spread"
            )


            result["contracts"] = calls[:2]


            result["risk"] = (

                calls[0]["premium"]

                *

                100

            )


            result["reward"] = (

                (
                    calls[1]["strike"]

                    -

                    calls[0]["strike"]

                )

                *

                100

                -

                result["risk"]

            )


        else:


            result["strategy"] = (
                "NO OPTIONS TRADE"
            )


        return result