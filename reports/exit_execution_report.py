def generate_exit_execution_report(data):


    print("\n")

    print("="*60)

    print("EXIT EXECUTION REPORT")

    print("="*60)



    print(

        "Status:",

        data.get("status")

    )


    print(

        "Reason:",

        data.get("reason")

    )



    if data.get("trade"):


        print("\nTrade:")


        for k,v in data["trade"].items():

            print(

                k,

                ":",

                v

            )


    print("="*60)