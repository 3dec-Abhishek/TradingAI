import json
import os
from datetime import datetime


class TradeMemory:


    def __init__(self):

        self.file = "data/trades.json"

        self.initialize()



    def initialize(self):

        if not os.path.exists(self.file):

            with open(self.file,"w") as f:

                json.dump([],f)



    def save_trade(self, trade):

        with open(self.file,"r") as f:

            history = json.load(f)



        trade["timestamp"] = str(datetime.now())


        history.append(trade)



        with open(self.file,"w") as f:

            json.dump(
                history,
                f,
                indent=4
            )



    def get_history(self):

        with open(self.file,"r") as f:

            return json.load(f)