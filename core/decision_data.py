from dataclasses import dataclass



@dataclass
class DecisionData:


    symbol:str

    action:str

    strategy:str

    confidence:float

    regime:str


    quantity:int=0


    reason:list=None



    def to_dict(self):


        return {


            "symbol":
            self.symbol,


            "action":
            self.action,


            "strategy":
            self.strategy,


            "confidence":
            self.confidence,


            "regime":
            self.regime,


            "quantity":
            self.quantity,


            "reason":
            self.reason or []

        }