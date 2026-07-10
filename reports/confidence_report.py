def generate_confidence_report(result):


    print("\n")

    print("=" * 50)

    print("AI CONFIDENCE ADJUSTMENT")

    print("=" * 50)



    for action, value in result.items():


        print(

            action,

            ":",

            value

        )



    print("=" * 50)