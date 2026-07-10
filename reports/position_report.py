def generate_position_report(report):

    print("\n")

    print("=" * 50)
    print("OPEN POSITIONS")
    print("=" * 50)

    if len(report) == 0:

        print("\nNo open positions.\n")

        print("=" * 50)

        return

    for position in report:

        pnl = position["pnl"]

        print(f"Symbol        : {position['symbol']}")
        print(f"Current Price : ${position['price']:.2f}")
        print(f"Status        : {position['status']}")
        print(f"Action        : {position['action']}")
        print(f"Profit ($)    : {pnl['profit']}")
        print(f"Profit (%)    : {pnl['percent']}%")
        print(f"Held (Hours)  : {pnl['holding_hours']}")

        print("-" * 50)

    print("=" * 50)