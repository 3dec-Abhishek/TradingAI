def generate_position_size_report(data):


    print("\n")

    print("="*55)

    print("POSITION SIZE ANALYSIS")

    print("="*55)



    print(

        "Recommended Quantity:",

        data["quantity"]

    )


    print(

        "Risk Amount:",

        data["risk_amount"]

    )


    print(

        "Confidence:",

        data["confidence"]

    )


    print(

        "Volatility:",

        data["volatility"]

    )


    print("="*55)