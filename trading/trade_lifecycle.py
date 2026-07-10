class TradeLifecycleManager:


    def __init__(self):

        self.open_trades = {}



    def open_trade(

        self,

        trade

    ):


        symbol = trade["symbol"]


        self.open_trades[symbol] = {


            "symbol":

            symbol,


            "action":

            trade["action"],


            "quantity":

            trade["quantity"],


            "entry_price":

            trade["price"],


            "status":

            "OPEN"

        }



        return self.open_trades[symbol]





    def update_trade(

        self,

        symbol,

        current_price

    ):


        if symbol not in self.open_trades:


            return {


                "status":

                "NO TRADE"

            }



        trade = self.open_trades[symbol]



        entry = trade["entry_price"]



        pnl = (

            current_price -

            entry

        ) * trade["quantity"]



        pnl_percent = (

            (

                current_price -

                entry

            )

            /

            entry

        ) * 100




        trade["current_price"] = current_price


        trade["pnl"] = round(

            pnl,

            2

        )


        trade["pnl_percent"] = round(

            pnl_percent,

            2

        )



        return trade





    def close_trade(

        self,

        symbol,

        price

    ):


        if symbol not in self.open_trades:


            return None



        trade = self.open_trades[symbol]



        trade["exit_price"] = price


        trade["status"] = "CLOSED"



        return trade