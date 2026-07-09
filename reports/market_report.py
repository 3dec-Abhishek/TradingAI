def generate_market_report(data):

    print("\n")
    print("="*50)
    print("Market Analysis")
    print("="*50)


    print(
        "Symbol:",
        data["symbol"]
    )


    print(
        "Price:",
        data["price"]
    )


    print(
        "RSI:",
        data["rsi"]
    )


    print(
        "20 Day SMA:",
        data["sma20"]
    )


    print(
        "50 Day SMA:",
        data["sma50"]
    )


    print("="*50)
