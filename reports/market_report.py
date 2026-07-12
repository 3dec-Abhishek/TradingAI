def generate_market_report(data):

    print("\n")
    print("=" * 50)
    print("Market Analysis")
    print("=" * 50)

    print("Symbol:", data.get("symbol", "N/A"))
    print("Price:", data.get("price", "N/A"))
    print("RSI:", data.get("rsi", "N/A"))

    sma20 = data.get(
        "sma20",
        data.get("20_day_sma", "N/A")
    )

    sma50 = data.get(
        "sma50",
        data.get("50_day_sma", "N/A")
    )

    print("20 Day SMA:", sma20)
    print("50 Day SMA:", sma50)

    print(
        "Volume:",
        data.get("volume", "N/A")
    )

    print(
        "Volatility:",
        data.get("volatility", "N/A")
    )

    print("=" * 50)