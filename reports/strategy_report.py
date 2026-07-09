def generate_strategy_report(results):


    print("\n")

    print("="*50)

    print("Strategy Analysis")

    print("="*50)



    for r in results:


        print(
            "\nStrategy:",
            r["strategy"]
        )


        print(
            "Signal:",
            r["signal"]
        )


        print(
            "Confidence:",
            r["confidence"],
            "%"
        )


        print(
            "Reason:",
            r["reason"]
        )


    print("="*50)
