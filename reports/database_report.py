def generate_database_report(history):


    print("\n")

    print("=" * 50)

    print("TRADE DATABASE MEMORY")

    print("=" * 50)



    print(

        "Stored Trades:",

        len(history)

    )



    for trade in history[:5]:


        print(

            trade["symbol"],

            trade["action"],

            trade["status"]

        )



    print("=" * 50)