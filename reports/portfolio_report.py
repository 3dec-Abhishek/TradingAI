def generate_report(data):

    print("\n")
    print("="*50)
    print("Portfolio Analysis Report")
    print("="*50)


    account = data["account"]

    print(
        f"Portfolio Value: ${account['portfolio_value']}"
    )

    print(
        f"Cash: ${account['cash']}"
    )


    print("\nPositions:")


    for p in data["positions"]:

        print(
            f"{p['symbol']} "
            f"{p['quantity']} shares "
            f"{p['gain_percent']}%"
        )


    print("\nRisk:")
    print(
        "Largest Position:",
        data["largest_position"]
    )

    print(
        "Risk Level:",
        data["risk"]
    )

    print("="*50)
