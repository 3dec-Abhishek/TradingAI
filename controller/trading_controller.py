from datetime import datetime


class TradingController:


    def __init__(self, engine):

        self.engine = engine

        self.running = True

        self.cycle = 0



    def run_cycle(self):

        self.cycle += 1


        print("\n")
        print("="*60)
        print(
            f"AUTONOMOUS CYCLE {self.cycle}"
        )
        print(
            datetime.now()
        )
        print("="*60)



        result = self.engine.run()


        self.process_result(
            result
        )


        return result



    def process_result(self,result):


        if not result:

            print(
                "No trading result"
            )

            return



        decision = result.get(
            "decision",
            {}
        )


        print("\nSYSTEM DECISION")

        print(
            decision
        )



        if decision.get(
            "action"
        )=="BUY":


            print(
                "BUY EXECUTED"
            )


        elif decision.get(
            "action"
        )=="SELL":


            print(
                "SELL EXECUTED"
            )


        else:


            print(
                "NO ACTION"
            )