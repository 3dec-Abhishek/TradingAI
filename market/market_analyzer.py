from market.indicators import add_indicators



class MarketAnalyzer:


    def analyze(
            self,
            data
        ):


        data = add_indicators(data)


        latest = data.iloc[-1]


        analysis = {

            "price":
                float(latest["Close"]),

            "rsi":
                round(
                    float(latest["RSI"]),
                    2
                ),

            "sma20":
                round(
                    float(latest["SMA20"]),
                    2
                ),

            "sma50":
                round(
                    float(latest["SMA50"]),
                    2
                )

        }


        return analysis
