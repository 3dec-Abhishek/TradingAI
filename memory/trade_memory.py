class TradeMemory:


    def __init__(self):

        self.trades=[]



    def store(self,trade):

        self.trades.append(
            trade
        )



    def history(self):

        return self.trades