from dataclasses import dataclass



@dataclass
class SignalData:


    strategy:str

    signal:str

    confidence:float


    reason:str=""


    def to_dict(self):

        return {


            "strategy":
            self.strategy,


            "signal":
            self.signal,


            "confidence":
            self.confidence,


            "reason":
            self.reason

        }