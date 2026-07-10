def generate_trade_report(result):


    print("\n")

    print("=" * 50)

    print("TRADE DECISION")

    print("=" * 50)



    print(

        "Status:",

        result.get(

            "status",

            "UNKNOWN"

        )

    )


    print(

        "Action:",

        result.get(

            "action",

            "NONE"

        )

    )


    print(

        "Symbol:",

        result.get(

            "symbol",

            "NONE"

        )

    )


    print(

        "Quantity:",

        result.get(

            "quantity",

            0

        )

    )


    print(

        "Price:",

        result.get(

            "price",

            0

        )

    )


    print("=" * 50)