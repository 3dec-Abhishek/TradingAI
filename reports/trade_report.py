def generate_trade_report(result):


    print("\n")
    print("="*50)
    print("TRADE DECISION")
    print("="*50)


    print(
        "Action:",
        result["action"]
    )


    print(
        "Reason:",
        result["reason"]
    )


    if result["trade"]:

        print(
            "Trade:",
            result["trade"]
        )


    print("="*50)