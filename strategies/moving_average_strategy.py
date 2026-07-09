from strategies.base_strategy import BaseStrategy


class MovingAverageStrategy(BaseStrategy):


    def analyze(self, market_data):


        price = market_data["price"]
        sma20 = market_data["sma20"]
        sma50 = market_data["sma50"]


        if sma20 > sma50 and price > sma20:

            return {

                "strategy":
                "Moving Average",

                "signal":
                "BUY",

                "confidence":
                65,

                "reason":
                "Price above moving averages"
            }


        elif sma20 < sma50:

            return {

                "strategy":
                "Moving Average",

                "signal":
                "SELL",

                "confidence":
                65,

                "reason":
                "Short term trend weakening"
            }


        return {

            "strategy":
            "Moving Average",

            "signal":
            "HOLD",

            "confidence":
            40,

            "reason":
            "No clear trend"

        }
