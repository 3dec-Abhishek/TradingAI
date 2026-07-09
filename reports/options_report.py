def generate_options_report(result):


    print("\n")
    print("="*50)
    print("OPTIONS ANALYSIS")
    print("="*50)


    print(
        "Symbol:",
        result["symbol"]
    )


    print(
        "Strategy:",
        result["strategy"]
    )


    print(
        "Risk:",
        result["risk"]
    )


    print(
        "Reward:",
        result["reward"]
    )


    print(
        "Contracts:"
    )


    for contract in result["contracts"]:

        print(contract)


    print("="*50)