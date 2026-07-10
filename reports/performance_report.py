def generate_performance_report(tracker):

    print()
    print("=" * 60)
    print("PERFORMANCE REPORT")
    print("=" * 60)

    trades = tracker.get_all_trades()

    print(f"Total Trades : {tracker.total_trades()}")
    print(f"Winning      : {tracker.winning_trades()}")
    print(f"Losing       : {tracker.losing_trades()}")
    print(f"Win Rate     : {tracker.win_rate()} %")
    print(f"Total Profit : ${tracker.total_profit()}")
    print(f"Avg Profit   : ${tracker.average_profit()}")

    print("=" * 60)