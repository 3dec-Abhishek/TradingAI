from collections import defaultdict


class StrategyTracker:

    def __init__(self, tracker):

        self.tracker = tracker

    ##################################################

    def analyze(self):

        trades = self.tracker.get_all_trades()

        grouped = defaultdict(list)

        for trade in trades:

            strategy = trade.get(
                "strategy",
                "UNKNOWN"
            )

            grouped[strategy].append(
                trade
            )

        report = {}

        for strategy, history in grouped.items():

            wins = len(

                [

                    trade

                    for trade in history

                    if trade["profit"] > 0

                ]

            )

            losses = len(history) - wins

            total_profit = round(

                sum(

                    trade["profit"]

                    for trade in history

                ),

                2

            )

            average_profit = 0

            if len(history):

                average_profit = round(

                    total_profit

                    / len(history),

                    2

                )

            report[strategy] = {

                "trades": len(history),

                "wins": wins,

                "losses": losses,

                "win_rate": round(

                    wins

                    / len(history)

                    * 100,

                    2

                ) if history else 0,

                "total_profit": total_profit,

                "average_profit": average_profit

            }

        return report