from dataclasses import dataclass



@dataclass
class TradeData:


    symbol:str


    action:str


    quantity:int


    price:float


    status:str



    def to_dict(self):


        return {


            "symbol":
            self.symbol,


            "action":
            self.action,


            "quantity":
            self.quantity,


            "price":
            self.price,


            "status":
            self.status

        }