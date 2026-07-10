from engine.trading_engine import TradingEngine



def main():

    print(
        "\nStarting Trading AI System...\n"
    )


    engine = TradingEngine()


    result = engine.run()



    print("\n")
    print("=" * 60)
    print("TRADING CYCLE COMPLETE")
    print("=" * 60)



    print(
        "Decision:",
        result["decision"]
    )


    print(
        "Trade:",
        result["trade"]
    )


    print("=" * 60)



if __name__ == "__main__":

    main()
