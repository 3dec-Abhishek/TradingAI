import warnings
import traceback

try:
    from urllib3.exceptions import NotOpenSSLWarning

    warnings.filterwarnings(
        "ignore",
        category=NotOpenSSLWarning
    )
except Exception:
    pass


from engine.bot_runner import TradingBot


def main():

    print("\n" + "=" * 60)
    print("TRADING AI SYSTEM")
    print("=" * 60)

    try:

        bot = TradingBot()

        bot.start()

    except KeyboardInterrupt:

        print("\nTrading Bot stopped by user.")

    except Exception as e:     
         print("\n" + "=" * 60)
         print("APPLICATION ERROR")
         print("=" * 60)
         traceback.print_exc()
         print("=" * 60)


if __name__ == "__main__":

    main()