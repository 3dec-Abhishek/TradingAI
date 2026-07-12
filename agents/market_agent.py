from unittest import result

import yfinance as yf
import pandas as pd
import numpy as np
from indicators.technical_engine import TechnicalEngine


class MarketAgent:


    def __init__(self):

        self.name = "Market Agent"
        self.technical = TechnicalEngine()



    def analyze(self, symbol="AAPL"):

        """
        Generic market analysis entry point.

        Used by TradingEngine.
        """

        return self.analyze_symbol(symbol)



    def analyze_symbol(self, symbol):

        """
        Analyze individual stock.
        """

        try:

            ticker = yf.Ticker(symbol)

            data = ticker.history(
                period="6mo"
            )

            technical = self.technical.calculate(data)

            if data.empty:

                raise Exception(
                    f"No market data available for {symbol}"
                )


            price = float(
                data["Close"].iloc[-1]
            )


            # Moving averages

            sma20 = float(
                data["Close"]
                .rolling(20)
                .mean()
                .iloc[-1]
            )


            sma50 = float(
                data["Close"]
                .rolling(50)
                .mean()
                .iloc[-1]
            )


            # RSI

            rsi = self.calculate_rsi(
                data["Close"]
            )



            # Volatility

            volatility = float(
                data["Close"]
                .pct_change()
                .std()
                *
                np.sqrt(252)
            )


            trend = self.detect_trend(
                price,
                sma20,
                sma50
            )

            result.update(
                technical
            )

            return {


                "symbol": symbol,


                "price": round(
                    price,
                    4
                ),


                "rsi": round(
                    rsi,
                    2
                ),


                "sma20": round(
                    sma20,
                    2
                ),


                "sma50": round(
                    sma50,
                    2
                ),

                "20_day_sma": round(
                    sma20,
                    2
                ),
                "50_day_sma": round(
                    sma50,
                    2
                ),


                "volatility": round(
                    volatility,
                    4
                ),


                "trend": trend,


                "timestamp":
                    str(
                        data.index[-1]
                    )

            }



        except Exception as e:


            print(
                "Market Agent Error:",
                e
            )


            return {


                "symbol": symbol,

                "price": 0,

                "rsi": 50,
                "sma20": 0,
                "sma50": 0,
                "20_day_sma": 0,

                "50_day_sma": 0,

                "volatility": 0,

                "trend": "UNKNOWN"

            }




    def calculate_rsi(
            self,
            prices,
            period=14
    ):


        delta = prices.diff()


        gain = delta.clip(
            lower=0
        )


        loss = -delta.clip(
            upper=0
        )


        avg_gain = (
            gain
            .rolling(period)
            .mean()
        )


        avg_loss = (
            loss
            .rolling(period)
            .mean()
        )


        rs = avg_gain / avg_loss


        rsi = (
            100 -
            (100 /
             (1 + rs))
        )


        value = rsi.iloc[-1]


        if pd.isna(value):

            return 50


        return float(value)




    def detect_trend(
            self,
            price,
            sma20,
            sma50
    ):


        if price > sma20 > sma50:

            return "BULLISH"


        elif price < sma20 < sma50:

            return "BEARISH"


        else:

            return "SIDEWAYS"