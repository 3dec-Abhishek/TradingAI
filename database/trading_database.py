import sqlite3
from datetime import datetime



class TradingDatabase:


    def __init__(self):


        self.connection = sqlite3.connect(

            "trading_history.db"

        )


        self.create_table()




    def create_table(self):


        cursor = self.connection.cursor()


        cursor.execute(

            """

            CREATE TABLE IF NOT EXISTS trades

            (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT,

                action TEXT,

                quantity INTEGER,

                price REAL,

                status TEXT,

                success INTEGER,

                created_at TEXT

            )

            """

        )


        self.connection.commit()




    def save_trade(

        self,

        trade

    ):


        cursor = self.connection.cursor()


        cursor.execute(

            """

            INSERT INTO trades

            (

                symbol,

                action,

                quantity,

                price,

                status,

                success,

                created_at

            )

            VALUES (?,?,?,?,?,?,?)

            """,

            (

                trade.get("symbol"),

                trade.get("action"),

                trade.get("quantity",0),

                trade.get("price",0),

                trade.get("status"),

                1 if trade.get("success") else 0,

                datetime.now().isoformat()

            )

        )


        self.connection.commit()




    def get_trades(self):


        cursor = self.connection.cursor()


        cursor.execute(

            """

            SELECT

            symbol,

            action,

            quantity,

            price,

            status,

            success,

            created_at

            FROM trades

            ORDER BY id DESC

            """

        )


        rows = cursor.fetchall()



        trades = []



        for row in rows:


            trades.append(

                {

                "symbol":row[0],

                "action":row[1],

                "quantity":row[2],

                "price":row[3],

                "status":row[4],

                "success":bool(row[5]),

                "created_at":row[6]

                }

            )


        return trades