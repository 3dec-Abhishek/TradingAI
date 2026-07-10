class MarketRegimeDetector:


    def __init__(self):

        self.regime = "UNKNOWN"

        self.last_analysis = {}



    def analyze(self, market):


        price = market.get(
            "price",
            0
        )


        sma20 = market.get(
            "sma20",
            market.get(
                "20_day_sma",
                price
            )
        )


        sma50 = market.get(
            "sma50",
            market.get(
                "50_day_sma",
                price
            )
        )


        rsi = market.get(
            "rsi",
            50
        )


        volatility = market.get(
            "volatility",
            0
        )



        if volatility > 5:


            self.regime = "HIGH_VOLATILITY"



        elif price > sma20 and sma20 > sma50:


            self.regime = "BULLISH"



        elif price < sma20 and sma20 < sma50:


            self.regime = "BEARISH"



        else:


            self.regime = "SIDEWAYS"



        self.last_analysis = {


            "regime": self.regime,


            "price": price,


            "rsi": rsi,


            "volatility": volatility,


            "description": self.get_regime_description()

        }


        return self.last_analysis





    def get_regime_description(self):


        descriptions = {


            "BULLISH":
            "Market is trending upward. Favor momentum strategies.",



            "BEARISH":
            "Market is trending downward. Reduce exposure and avoid aggressive entries.",



            "SIDEWAYS":
            "Market lacks direction. Prefer conservative strategies.",



            "HIGH_VOLATILITY":
            "Market volatility is elevated. Reduce position size and increase risk controls.",



            "UNKNOWN":
            "Market regime is unknown."

        }


        return descriptions.get(

            self.regime,

            "Market condition unavailable."

        )



    # Backward compatibility

    def description(self):

        return self.get_regime_description()