import time
from datetime import datetime

from engine.trading_engine import TradingEngine
from config.trading_config import TRADING_INTERVAL


class TradingBot:

    def __init__(self):
        print("\nInitializing Trading Engine...\n")
        self.engine = TradingEngine()
        self.running = True
        self.cycle = 1

    def run_cycle(self):
        print("\n" + "=" * 60)
        print(f"TRADING CYCLE #{self.cycle}")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 60)

        result = self.engine.run()

        print("\nTrading cycle completed successfully.")

        self.cycle += 1

        return result

    def start(self):
        print("\n" + "=" * 60)
        print("AUTONOMOUS TRADING BOT STARTED")
        print("=" * 60)

        while self.running:
            try:
                self.run_cycle()

                print(f"\nWaiting {TRADING_INTERVAL} seconds until next cycle...")
                time.sleep(TRADING_INTERVAL)

            except KeyboardInterrupt:
                print("\nTrading bot stopped.")
                self.running = False

            except Exception as e:
                print("\n" + "=" * 60)
                print("TRADING ERROR")
                print("=" * 60)
                print(type(e).__name__)
                print(e)
                print("\nRetrying in 30 seconds...")
                time.sleep(30)


if __name__ == "__main__":
    bot = TradingBot()
    bot.start()