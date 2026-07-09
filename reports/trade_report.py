def generate_trade_report(result):


    print("\n")
    print("="*50)
    print("PAPER TRADE EXECUTION")
    print("="*50)


    for key,value in result.items():

        print(
            f"{key}: {value}"
        )


    print("="*50)