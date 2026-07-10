import json
import os
from datetime import datetime


class PerformanceTracker:

    def __init__(self):

        self.file = "data/trade_history.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f, indent=4)

        self.trades = self.load()

    # =============================================

    def load(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except Exception:

            return []

    # =============================================

    def save(self):

        with open(self.file, "w") as f:

            json.dump(self.trades, f, indent=4)

    # =============================================

    def add_trade(

        self,

        symbol,

        strategy,

        action,

        entry_price,

        exit_price,

        quantity,

        confidence,

        risk,

        ai_summary,

        market_condition="UNKNOWN"

    ):

        profit = (exit_price - entry_price) * quantity

        percent = 0

        if entry_price > 0:

            percent = round(

                ((exit_price - entry_price)

                / entry_price)

                * 100,

                2

            )

        trade = {

            "timestamp": datetime.now().isoformat(),

            "symbol": symbol,

            "strategy": strategy,

            "action": action,

            "entry_price": entry_price,

            "exit_price": exit_price,

            "quantity": quantity,

            "profit": round(profit, 2),

            "percent": percent,

            "confidence": confidence,

            "risk": risk,

            "market_condition": market_condition,

            "ai_summary": ai_summary

        }

        self.trades.append(trade)

        self.save()

        return trade

    # =============================================

    def get_all_trades(self):

        return self.trades

    # =============================================

    def total_profit(self):

        return round(

            sum(

                trade["profit"]

                for trade in self.trades

            ),

            2

        )

    # =============================================

    def total_trades(self):

        return len(self.trades)

    # =============================================

    def winning_trades(self):

        return len(

            [

                trade

                for trade in self.trades

                if trade["profit"] > 0

            ]

        )

    # =============================================

    def losing_trades(self):

        return len(

            [

                trade

                for trade in self.trades

                if trade["profit"] <= 0

            ]

        )

    # =============================================

    def win_rate(self):

        if len(self.trades) == 0:

            return 0

        return round(

            self.winning_trades()

            / len(self.trades)

            * 100,

            2

        )

    # =============================================

    def average_profit(self):

        if len(self.trades) == 0:

            return 0

        return round(

            self.total_profit()

            / len(self.trades),

            2

        )