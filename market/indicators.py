
import ta


def add_indicators(data):


    close = data["Close"]


    data["RSI"] = (
        ta.momentum
        .RSIIndicator(
            close
        )
        .rsi()
    )


    data["SMA20"] = (
        close
        .rolling(20)
        .mean()
    )


    data["SMA50"] = (
        close
        .rolling(50)
        .mean()
    )


    return data