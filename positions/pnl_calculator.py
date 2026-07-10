from datetime import datetime


class PnLCalculator:

    @staticmethod
    def calculate(position):

        dollar_profit = (
            position.current_price
            - position.entry_price
        ) * 100 * position.contracts

        percent_profit = (
            (
                position.current_price
                - position.entry_price
            )
            / position.entry_price
        ) * 100

        entry = datetime.fromisoformat(
            position.entry_time
        )

        hours = (
            datetime.now() - entry
        ).total_seconds() / 3600

        return {

            "profit": round(
                dollar_profit,
                2
            ),

            "percent": round(
                percent_profit,
                2
            ),

            "holding_hours": round(
                hours,
                2
            )

        }