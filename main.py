import time


from engine.trading_engine import TradingEngine

from config.trading_config import TRADING_INTERVAL





class TradingBot:



    def __init__(self):


        self.engine = TradingEngine()



        self.running = True





    def start(self):


        print(

            "\nAUTONOMOUS TRADING BOT STARTED\n"

        )



        while self.running:



            try:



                result = self.engine.run()



                print(

                    "\nCycle finished"

                )



                print(

                    "Waiting for next cycle..."

                )



                time.sleep(

                    TRADING_INTERVAL

                )




            except KeyboardInterrupt:


                print(

                    "\nBot stopped manually"

                )


                self.running = False




            except Exception as e:


                print(

                    "\nTrading Error:",

                    e

                )



                time.sleep(

                    30

                )