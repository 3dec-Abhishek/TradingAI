def generate_monitor_report(

    result

):


    print("\n")

    print("=" * 50)

    print("PORTFOLIO MONITOR")

    print("=" * 50)



    print(

        "Status:",

        result.get(

            "status",

            "UNKNOWN"

        )

    )



    print("\nMetrics:")



    for key,value in result.get(

        "metrics",

        {}

    ).items():


        print(

            key,

            ":",

            value

        )



    print("\nAlerts:")



    alerts = result.get(

        "alerts",

        []

    )


    if not alerts:


        print(

            "No risk alerts"

        )


    else:


        for alert in alerts:


            print(

                "-",

                alert

            )



    print("=" * 50)