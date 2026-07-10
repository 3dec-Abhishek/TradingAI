class Metrics:

    @staticmethod
    def total_profit(trades):

        return round(

            sum(

                trade.get("profit", 0)

                for trade in trades

            ),

            2

        )

    ##################################################

    @staticmethod
    def average_profit(trades):

        if len(trades) == 0:

            return 0

        return round(

            Metrics.total_profit(trades)

            / len(trades),

            2

        )

    ##################################################

    @staticmethod
    def win_rate(trades):

        if len(trades) == 0:

            return 0

        wins = len(

            [

                t

                for t in trades

                if t.get("profit", 0) > 0

            ]

        )

        return round(

            wins

            / len(trades)

            * 100,

            2

        )

    ##################################################

    @staticmethod
    def average_return(trades):

        if len(trades) == 0:

            return 0

        values = [

            trade.get("percent", 0)

            for trade in trades

        ]

        return round(

            sum(values)

            / len(values),

            2

        )

    ##################################################

    @staticmethod
    def largest_win(trades):

        if len(trades) == 0:

            return 0

        return max(

            trade.get("profit", 0)

            for trade in trades

        )

    ##################################################

    @staticmethod
    def largest_loss(trades):

        if len(trades) == 0:

            return 0

        return min(

            trade.get("profit", 0)

            for trade in trades

        )

    ##################################################

    @staticmethod
    def profit_factor(trades):

        gross_profit = sum(

            t.get("profit", 0)

            for t in trades

            if t.get("profit", 0) > 0

        )

        gross_loss = abs(

            sum(

                t.get("profit", 0)

                for t in trades

                if t.get("profit", 0) < 0

            )

        )

        if gross_loss == 0:

            return float("inf")

        return round(

            gross_profit

            / gross_loss,

            2

        )