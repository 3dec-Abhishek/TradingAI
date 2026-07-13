from dataclasses import dataclass



@dataclass
class RiskData:


    status:str


    risk_level:str


    max_position:float


    message:str=""


    def to_dict(self):

        return {


            "status":
            self.status,


            "risk_level":
            self.risk_level,


            "max_position":
            self.max_position,


            "message":
            self.message

        }