import sqlite3


DATABASE_NAME = "trading.db"



class Database:


    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE_NAME
        )

        self.cursor = self.connection.cursor()


        self.create_tables()



    def create_tables(self):

        self.cursor.execute(
            """

            CREATE TABLE IF NOT EXISTS trades (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT,

                action TEXT,

                quantity INTEGER,

                price REAL,

                confidence INTEGER,

                strategy TEXT,

                result TEXT,

                profit REAL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """
        )



        self.cursor.execute(
            """

            CREATE TABLE IF NOT EXISTS positions (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT,

                quantity INTEGER,

                average_price REAL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """
        )



        self.cursor.execute(
            """

            CREATE TABLE IF NOT EXISTS performance (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                total_trades INTEGER,

                winning_trades INTEGER,

                losing_trades INTEGER,

                total_profit REAL,

                win_rate REAL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """
        )


        self.connection.commit()



    def execute(

        self,

        query,

        params=()

    ):

        self.cursor.execute(

            query,

            params

        )

        self.connection.commit()



    def fetch_all(

        self,

        query,

        params=()

    ):

        self.cursor.execute(

            query,

            params

        )

        return self.cursor.fetchall()