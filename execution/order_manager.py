class OrderManager:


    def __init__(self, broker):

        self.broker = broker



    def execute_trade(self, trade):

        result = self.broker.place_order(
            trade
        )

        return result
