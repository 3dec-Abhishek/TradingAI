class TradingState:


    def __init__(self):

        self.state={

            "market":None,

            "signals":None,

            "decision":None,

            "positions":{},

            "last_trade":None,

            "errors":[]

        }



    def update(
        self,
        key,
        value
    ):

        self.state[key]=value



    def get(
        self,
        key
    ):

        return self.state.get(
            key
        )



    def snapshot(self):

        return self.state.copy()