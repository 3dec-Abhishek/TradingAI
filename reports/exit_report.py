def generate_exit_report(data):


    print("\n")

    print("="*55)

    print("EXIT MANAGEMENT REPORT")

    print("="*55)



    print(

        "Action:",

        data.get("action")

    )



    print(

        "Reason:",

        data.get("reason")

    )



    if "levels" in data:


        print("\nLevels:")



        print(

            "Entry:",

            data["levels"]["entry"]

        )


        print(

            "Stop Loss:",

            data["levels"]["stop_loss"]

        )


        print(

            "Take Profit:",

            data["levels"]["take_profit"]

        )



    print("="*55)