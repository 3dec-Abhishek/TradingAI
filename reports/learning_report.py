def generate_learning_report(

    learning_result

):


    print("\n")

    print("=" * 60)

    print("AI LEARNING PERFORMANCE REPORT")

    print("=" * 60)



    # =========================
    # Status
    # =========================


    print(

        "Learning Status:",

        learning_result.get(

            "status",

            "UNKNOWN"

        )

    )



    print("\nPerformance Metrics:")



    metrics = learning_result.get(

        "metrics",

        {}

    )



    if not metrics:


        print(

            "No performance data available"

        )


    else:


        for key, value in metrics.items():


            print(

                f"{key}: {value}"

            )




    print("\nAI Feedback:")



    feedback = learning_result.get(

        "feedback",

        []

    )



    if not feedback:


        print(

            "No learning feedback generated"

        )


    else:


        for item in feedback:


            print(

                "-",

                item

            )



    print("=" * 60)