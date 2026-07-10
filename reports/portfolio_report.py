def generate_report(portfolio):


    print("\n")
    print("=" * 50)
    print("Portfolio Analysis Report")
    print("=" * 50)



    # =========================
    # Account Information
    # =========================

    account = portfolio.get(
        "account",
        {}
    )


    print(
        f"Portfolio Value: ${account.get('portfolio_value', 0)}"
    )


    print(
        f"Cash: ${account.get('cash', 0)}"
    )



    print("\nPositions:")



    # =========================
    # Positions
    # =========================

    positions = portfolio.get(
        "positions",
        []
    )


    if not positions:


        print(
            "No open positions"
        )


    else:


        for position in positions:


            symbol = position.get(
                "symbol",
                "UNKNOWN"
            )


            quantity = position.get(
                "quantity",
                0
            )


            gain = position.get(
                "gain_percent",
                0
            )


            value = position.get(
                "value",
                0
            )


            average_price = position.get(
                "average_price",
                0
            )


            print(

                f"{symbol} | "
                f"Shares: {quantity} | "
                f"Value: ${value} | "
                f"Avg Price: ${average_price} | "
                f"Gain: {gain}%"

            )



    print("\nRisk:")



    print(

        f"Largest Position: "
        f"{portfolio.get('largest_position', 'None')}"

    )


    print(

        f"Risk Level: "
        f"{portfolio.get('risk', 'UNKNOWN')}"

    )



    print("=" * 50)