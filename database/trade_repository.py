from database.db import Database



class TradeRepository:


    def __init__(self):

        self.db = Database()



    def save_trade(

        self,

        trade

    ):


        self.db.execute(

            """

            INSERT INTO trades

            (

                symbol,

                action,

                quantity,

                price,

                confidence,

                strategy,

                result,

                profit

            )

            VALUES (?,?,?,?,?,?,?,?)

            """,

            (

                trade.get(
                    "symbol"
                ),

                trade.get(
                    "action"
                ),

                trade.get(
                    "quantity",
                    0
                ),

                trade.get(
                    "price",
                    0
                ),

                trade.get(
                    "confidence",
                    0
                ),

                trade.get(
                    "strategy",
                    "AI"
                ),

                trade.get(
                    "status"
                ),

                trade.get(
                    "profit",
                    0
                )

            )

        )



    def get_trades(self):

        return self.db.fetch_all(

            """

            SELECT *

            FROM trades

            ORDER BY id DESC

            """

        )