def generate_decision_report(result):


    print("\n")
    print("="*50)
    print("FINAL TRADING DECISION")
    print("="*50)


    print(
        f"""
Symbol:
{result['symbol']}


Action:
{result['action']}


Confidence:
{result['confidence']}%


Reason:
"""
    )


    for reason in result["reason"]:

        print("-", reason)


    print("="*50)