from strategies.base_strategy import BaseStrategy


class RSIStrategy(BaseStrategy):


    def analyze(self, market_data):

        rsi = market_data["rsi"]


        if rsi < 30:

            return {
                "strategy": "RSI",
                "signal": "BUY",
                "confidence": 70,
                "reason":
                "RSI indicates oversold condition"
            }


        elif rsi > 70:

            return {
                "strategy": "RSI",
                "signal": "SELL",
                "confidence": 70,
                "reason":
                "RSI indicates overbought condition"
            }


        return {
            "strategy": "RSI",
            "signal": "HOLD",
            "confidence": 40,
            "reason":
            "RSI is neutral"
        }
