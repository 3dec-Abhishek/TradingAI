class ExecutionManager:


    def __init__(self,order_manager):

        self.order_manager=order_manager



    def execute(self,decision,market):


        if decision["action"]=="HOLD":

            return {

                "status":"NO TRADE"

            }



        return self.order_manager.execute(

            decision,

            market

        )