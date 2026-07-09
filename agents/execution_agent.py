from execution.paper_broker import PaperBroker
from execution.order_manager import OrderManager
from execution.trade_logger import TradeLogger



class ExecutionAgent:


    def __init__(self):

        self.broker = PaperBroker()

        self.manager = OrderManager(
            self.broker
        )

        self.logger = TradeLogger()



    def execute(self, trade):


        result = self.manager.execute_trade(
            trade
        )


        self.logger.log(
            result
        )


        return result