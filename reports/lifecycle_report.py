def generate_lifecycle_report(data):


    print("\n")

    print("=" * 60)

    print("TRADE LIFECYCLE REPORT")

    print("=" * 60)



    if data is None:


        print("No lifecycle data available")


        print("=" * 60)


        return



    for key, value in data.items():


        print(

            f"{key}: {value}"

        )



    print("=" * 60)