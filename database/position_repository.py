from database.db import Database



class PositionRepository:


    def __init__(self):

        self.db = Database()



    def get_positions(self):

        return self.db.fetch_all(

            """

            SELECT

                symbol,

                quantity,

                average_price

            FROM positions

            """

        )



    def get_position(

        self,

        symbol

    ):


        result = self.db.fetch_all(

            """

            SELECT

                symbol,

                quantity,

                average_price

            FROM positions

            WHERE symbol = ?

            """,

            (

                symbol,

            )

        )


        if result:

            return result[0]


        return None



    def add_position(

        self,

        symbol,

        quantity,

        price

    ):


        existing = self.get_position(

            symbol

        )


        if existing:


            old_quantity = existing[1]

            old_price = existing[2]


            new_quantity = (

                old_quantity +

                quantity

            )


            new_average = (

                (

                    old_quantity * old_price

                )

                +

                (

                    quantity * price

                )

            ) / new_quantity



            self.db.execute(

                """

                UPDATE positions

                SET

                quantity = ?,

                average_price = ?

                WHERE symbol = ?

                """,

                (

                    new_quantity,

                    new_average,

                    symbol

                )

            )


        else:


            self.db.execute(

                """

                INSERT INTO positions

                (

                    symbol,

                    quantity,

                    average_price

                )

                VALUES (?,?,?)

                """,

                (

                    symbol,

                    quantity,

                    price

                )

            )



    def remove_position(

        self,

        symbol,

        quantity

    ):


        existing = self.get_position(

            symbol

        )


        if not existing:

            return



        current_quantity = existing[1]


        remaining = (

            current_quantity -

            quantity

        )


        if remaining <= 0:


            self.db.execute(

                """

                DELETE FROM positions

                WHERE symbol = ?

                """,

                (

                    symbol,

                )

            )


        else:


            self.db.execute(

                """

                UPDATE positions

                SET quantity = ?

                WHERE symbol = ?

                """,

                (

                    remaining,

                    symbol

                )

            )