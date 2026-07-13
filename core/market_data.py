from dataclasses import dataclass


@dataclass
class MarketData:


    symbol:str

    price:float

    rsi:float

    sma20:float

    sma50:float

    volatility:float

    trend:str


    volume:float = 0

    timestamp:str = ""



    def to_dict(self):

        return {

            "symbol":self.symbol,

            "price":self.price,

            "rsi":self.rsi,

            "sma20":self.sma20,

            "sma50":self.sma50,

            "volatility":self.volatility,

            "trend":self.trend,

            "volume":self.volume,

            "timestamp":self.timestamp

        }