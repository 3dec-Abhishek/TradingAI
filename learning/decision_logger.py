import json
from datetime import datetime


class DecisionLogger:


    def __init__(self):

        self.file="data/decisions.json"


    def log(
        self,
        decision
    ):


        record={

            "time":
                str(datetime.now()),

            "decision":
                decision

        }


        try:

            with open(
                self.file,
                "a"
            ) as f:

                f.write(
                    json.dumps(record)
                    + "\n"
                )

        except Exception as e:

            print(
                "Decision log error:",
                e
            )