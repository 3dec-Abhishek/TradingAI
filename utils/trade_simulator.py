import random


class TradeSimulator:

    def evaluate(self):

        entry = round(
            random.uniform(2.0, 5.0),
            2
        )

        movement = random.uniform(
            -1.5,
            2.5
        )

        exit_price = round(
            entry + movement,
            2
        )

        quantity = 10

        profit = round(
            (exit_price - entry)
            * quantity,
            2
        )

        return {

            "entry": entry,

            "exit": exit_price,

            "quantity": quantity,

            "profit": profit

        }