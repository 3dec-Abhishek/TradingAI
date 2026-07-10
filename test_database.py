from database.db import Database


db = Database()


db.execute(

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
"AAPL",
"BUY",
1,
316.22,
65,
"RSI",
"FILLED",
0
)

)



print(

db.fetch_all(
    "SELECT * FROM trades"
)

)