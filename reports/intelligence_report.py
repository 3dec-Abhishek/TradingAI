def generate_intelligence_report(data):


    print("\n")

    print("=" * 55)

    print("TRADING INTELLIGENCE REPORT")

    print("=" * 55)



    print(

        "Total Trades:",

        data["total_trades"]

    )


    print(

        "Winning Trades:",

        data["winning_trades"]

    )


    print(

        "Losing Trades:",

        data["losing_trades"]

    )


    print(

        "Win Rate:",

        data["win_rate"],

        "%"

    )


    print(

        "BUY Trades:",

        data["buy_trades"]

    )


    print(

        "SELL Trades:",

        data["sell_trades"]

    )



    print("=" * 55)