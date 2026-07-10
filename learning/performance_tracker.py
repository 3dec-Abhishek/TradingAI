from memory.persistent_memory import PersistentMemory



class PerformanceTracker:


    def __init__(self):


        self.memory = PersistentMemory()


        self.history = self.memory.get_history()




    def record_trade(

        self,

        trade_result

    ):


        if not trade_result:


            return None



        status = trade_result.get(

            "status",

            "UNKNOWN"

        )


        action = trade_result.get(

            "action",

            "HOLD"

        )



        success = (

            status == "FILLED"

        )



        trade = {


            "symbol":

            trade_result.get(

                "symbol",

                ""

            ),


            "action":

            action,


            "quantity":

            trade_result.get(

                "quantity",

                0

            ),


            "price":

            trade_result.get(

                "price",

                0

            ),


            "status":

            status,


            "success":

            success

        }



        self.history.append(

            trade

        )



        self.memory.save_trade(

            trade

        )



        return trade





    def get_history(self):


        return self.history





    def get_statistics(self):


        total = len(

            self.history

        )



        if total == 0:


            return {


                "total_trades":0,

                "win_rate":0

            }



        wins = sum(

            1

            for trade in self.history

            if trade.get(

                "success"

            )

        )



        return {


            "total_trades":

            total,


            "winning_trades":

            wins,


            "win_rate":

            round(

                wins /

                total *

                100,

                2

            )

        }