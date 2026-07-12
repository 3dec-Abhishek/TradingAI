def generate_strategy_report(results):

    print("\n")
    print("=" * 50)
    print("STRATEGY REPORT")
    print("=" * 50)

    # Normalize to a list
    if isinstance(results, dict):
        results = [results]

    for r in results:
        print("Strategy   :", r.get("strategy", "UNKNOWN"))
        print("Signal     :", r.get("signal", r.get("action", "HOLD")))
        print("Confidence :", r.get("confidence", 0))
        print("-" * 50)