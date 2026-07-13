from execution.trading_mode import TradingMode



class LiveController:


    def __init__(self):

        self.mode = TradingMode.PAPER



    def enable_live(self):

        self.mode = TradingMode.LIVE



    def can_trade(self):


        return {


            "mode":

            self.mode,


            "approved":

            self.mode==TradingMode.LIVE

        }