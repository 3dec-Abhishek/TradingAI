from database.trading_database import TradingDatabase



class PersistentMemory:


    def __init__(self):

        self.database = TradingDatabase()




    def save_trade(

        self,

        trade

    ):


        self.database.save_trade(

            trade

        )




    def get_history(self):


        return self.database.get_trades()