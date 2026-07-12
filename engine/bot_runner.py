import time
from datetime import datetime


from engine.trading_engine import TradingEngine

from config.trading_config import TRADING_INTERVAL

from utils.system_health import SystemHealth
import traceback



class TradingBot:


    def __init__(self):


        self.engine = TradingEngine()


        self.health = SystemHealth(

            self.engine

        )


        self.running = True


        self.cycle = 1





    def run_cycle(self):


        print("\n" + "=" * 60)

        print(

            f"TRADING CYCLE #{self.cycle}"

        )

        print(

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        print("=" * 60)



        self.health.display()



        result = self.engine.run()



        print(

            "\nTrading cycle completed successfully."

        )



        self.cycle += 1



        return result





    def shutdown(self):


        print("\nSaving trading state...")


        try:


            if hasattr(
                self.engine,
                "performance_tracker"
            ):


                self.engine.performance_tracker.save()



        except Exception as e:


            print(
                "State save skipped:",
                e
            )



        print(
            "Trading bot stopped."
        )



        self.running = False





    def start(self):


        print("\n" + "=" * 60)

        print(
            "AUTONOMOUS TRADING BOT STARTED"
        )

        print("=" * 60)



        while self.running:


            try:


                self.run_cycle()



                print(

                    f"\nWaiting {TRADING_INTERVAL} seconds..."

                )


                time.sleep(

                    TRADING_INTERVAL

                )



            except KeyboardInterrupt:


                self.shutdown()



            except Exception as e:


                print("\nTRADING ERROR")

                print(
                    type(e).__name__,
                    e
                )

                traceback.print_exc()
                # print(
                #     "Retrying in 30 seconds..."
                # )


                time.sleep(30)





if __name__ == "__main__":


    bot = TradingBot()


    bot.start()