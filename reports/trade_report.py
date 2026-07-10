def generate_trade_report(result):


    print("\n")

    print("="*50)

    print("TRADE EXECUTION REPORT")

    print("="*50)



    print(

        "Status:",

        result.get("status")

    )


    print(

        "Action:",

        result.get("action")

    )


    print(

        "Symbol:",

        result.get("symbol")

    )


    print(

        "Quantity:",

        result.get("quantity")

    )


    print(

        "Price:",

        result.get("price")

    )



    if "portfolio" in result:


        print("\nPortfolio Update")


        print(

            "Cash:",

            result["portfolio"]["cash"]

        )


        print(

            "Positions:",

            result["portfolio"]["positions"]

        )



    print("="*50)