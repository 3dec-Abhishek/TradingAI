def generate_portfolio_account_report(data):


    print("\n")

    print("="*55)

    print("PORTFOLIO ACCOUNT REPORT")

    print("="*55)



    print(

        "Cash:",

        data["cash"]

    )



    print("\nPositions:")



    for symbol, position in data["positions"].items():


        print(

            symbol,

            position

        )



    print("="*55)