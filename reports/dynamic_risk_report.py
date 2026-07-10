def generate_dynamic_risk_report(data):


    print("\n")

    print("="*55)

    print("DYNAMIC RISK REPORT")

    print("="*55)



    print(

        "Status:",

        data["status"]

    )


    print(

        "Available Cash:",

        data["available_cash"]

    )


    print("\nChecks:")



    for name,value in data["checks"].items():


        print(

            name,

            ":",

            value["value"],

            "%",

            "/ Limit",

            value["limit"]

        )



    if data["failed"]:


        print(

            "Failed:",

            data["failed"]

        )


    print("="*55)