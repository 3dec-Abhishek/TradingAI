import sqlite3
from datetime import datetime



class EventStore:



    def __init__(self):

        self.db = sqlite3.connect(
            "events.db"
        )


        self.create()



    def create(self):

        self.db.execute(

        """
        CREATE TABLE IF NOT EXISTS events(

        id INTEGER PRIMARY KEY,

        event TEXT,

        data TEXT,

        timestamp TEXT

        )
        """

        )



    def save(
        self,
        event,
        data
    ):


        self.db.execute(

        """

        INSERT INTO events

        VALUES(NULL,?,?,?)

        """,

        (

        event,

        str(data),

        str(datetime.now())

        )

        )


        self.db.commit()