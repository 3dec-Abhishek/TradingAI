import pandas as pd
import numpy as np


class TechnicalEngine:


    def calculate(self, data):


        close = data["Close"]
        high = data["High"]
        low = data["Low"]
        volume = data["Volume"]


        result = {}



        # =========================
        # Moving Averages
        # =========================


        result["sma20"] = (
            close
            .rolling(20)
            .mean()
            .iloc[-1]
        )


        result["sma50"] = (
            close
            .rolling(50)
            .mean()
            .iloc[-1]
        )


        result["ema20"] = (
            close
            .ewm(span=20)
            .mean()
            .iloc[-1]
        )



        # =========================
        # MACD
        # =========================


        ema12 = (
            close
            .ewm(span=12)
            .mean()
        )


        ema26 = (
            close
            .ewm(span=26)
            .mean()
        )


        macd = ema12 - ema26


        result["macd"] = macd.iloc[-1]



        result["macd_signal"] = (

            macd
            .ewm(span=9)
            .mean()
            .iloc[-1]

        )



        # =========================
        # Bollinger Bands
        # =========================


        middle = (
            close
            .rolling(20)
            .mean()
        )


        std = (
            close
            .rolling(20)
            .std()
        )


        result["bb_upper"] = (
            middle + 2*std
        ).iloc[-1]


        result["bb_lower"] = (
            middle - 2*std
        ).iloc[-1]



        # =========================
        # ATR
        # =========================


        tr1 = high-low

        tr2 = abs(
            high-close.shift()
        )

        tr3 = abs(
            low-close.shift()
        )


        true_range = pd.concat(
            [
                tr1,
                tr2,
                tr3
            ],
            axis=1
        ).max(axis=1)


        result["atr"] = (

            true_range
            .rolling(14)
            .mean()
            .iloc[-1]

        )



        # =========================
        # VWAP
        # =========================


        result["vwap"] = (

            (
                close*volume
            )
            .cumsum()
            /
            volume.cumsum()

        ).iloc[-1]



        # =========================
        # Momentum
        # =========================


        result["momentum"] = (

            close.iloc[-1]
            -
            close.iloc[-10]

        )



        return result