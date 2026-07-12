def generate_execution_report(data):

    print("\n")
    print("=" * 50)
    print("EXECUTION REPORT")
    print("=" * 50)


    for key,value in data.items():

        print(
            f"{key}: {value}"
        )


    print("=" * 50)