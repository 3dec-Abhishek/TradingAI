from datetime import datetime


class Position:

    def __init__(
        self,
        symbol,
        asset_type="OPTION",
        option_type=None,
        strike=None,
        expiration=None,
        contracts=1,
        entry_price=0.0,
        stop_loss=None,
        take_profit=None,
    ):

        self.id = str(int(datetime.now().timestamp()))

        self.symbol = symbol
        self.asset_type = asset_type

        self.option_type = option_type
        self.strike = strike
        self.expiration = expiration

        self.contracts = contracts

        self.entry_price = float(entry_price)
        self.current_price = float(entry_price)

        self.entry_time = datetime.now().isoformat()

        self.status = "OPEN"

        self.stop_loss = stop_loss
        self.take_profit = take_profit

        self.pnl = 0.0

    def update_price(self, price):

        self.current_price = float(price)
        self.calculate_pnl()

    def calculate_pnl(self):

        self.pnl = (
            (self.current_price - self.entry_price)
            * 100
            * self.contracts
        )

        return self.pnl

    def close(self):

        self.status = "CLOSED"

    def to_dict(self):

        return {
            "id": self.id,
            "symbol": self.symbol,
            "asset_type": self.asset_type,
            "option_type": self.option_type,
            "strike": self.strike,
            "expiration": self.expiration,
            "contracts": self.contracts,
            "entry_price": self.entry_price,
            "current_price": self.current_price,
            "entry_time": self.entry_time,
            "status": self.status,
            "stop_loss": self.stop_loss,
            "take_profit": self.take_profit,
            "pnl": self.pnl,
        }

    @classmethod
    def from_dict(cls, data):

        obj = cls(
            symbol=data["symbol"],
            asset_type=data["asset_type"],
            option_type=data["option_type"],
            strike=data["strike"],
            expiration=data["expiration"],
            contracts=data["contracts"],
            entry_price=data["entry_price"],
            stop_loss=data["stop_loss"],
            take_profit=data["take_profit"],
        )

        obj.id = data["id"]
        obj.current_price = data["current_price"]
        obj.entry_time = data["entry_time"]
        obj.status = data["status"]
        obj.pnl = data["pnl"]

        return obj