def generate_valuation_report(data):


    print("\n")

    print("="*55)

    print("PORTFOLIO VALUATION REPORT")

    print("="*55)



    print(

        "Cash:",

        data["cash"]

    )



    print(

        "Position Value:",

        data["position_value"]

    )



    print(

        "Portfolio Value:",

        data["portfolio_value"]

    )



    print(

        "Unrealized P/L:",

        data["unrealized_pnl"]

    )



    print("\nPositions:")



    for symbol, position in data["positions"].items():


        print(

            symbol,

            position

        )



    print("="*55)