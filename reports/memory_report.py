def generate_memory_report(history):

    print("\n")
    print("="*50)
    print("TRADE MEMORY")
    print("="*50)


    for trade in history:

        print()

        print(
            "Symbol:",
            trade.get("symbol")
        )

        print(
            "Action:",
            trade.get("action")
        )

        print(
            "Confidence:",
            trade.get("confidence")
        )

        print(
            "Time:",
            trade.get("timestamp")
        )


    print("="*50)