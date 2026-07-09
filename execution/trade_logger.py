import json
import os


class TradeLogger:


    def __init__(self):

        self.file = "trades/history.json"



    def log(self, trade):


        os.makedirs(
            "trades",
            exist_ok=True
        )


        history=[]


        if os.path.exists(self.file):

            with open(self.file,"r") as f:

                history=json.load(f)



        history.append(trade)



        with open(self.file,"w") as f:

            json.dump(
                history,
                f,
                indent=4
            )