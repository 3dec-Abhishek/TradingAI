from orders.order_manager import OrderManager

from database.trade_repository import TradeRepository

from database.position_repository import PositionRepository



class ExecutionService:



    def __init__(

        self,

        broker

    ):


        self.order_manager = OrderManager(

            broker

        )


        self.trade_repository = TradeRepository()


        self.position_repository = PositionRepository()




    def execute(

        self,

        decision,

        market

    ):


        trade_result = (

            self.order_manager
            .execute(

                decision,

                market

            )

        )



        # Save trade history

        self.trade_repository.save_trade(

            trade_result

        )



        # Update positions

        if trade_result["status"] == "FILLED":


            action = trade_result["action"]


            if action == "BUY":


                self.position_repository.add_position(

                    trade_result["symbol"],

                    trade_result["quantity"],

                    trade_result["price"]

                )


            elif action == "SELL":


                self.position_repository.remove_position(

                    trade_result["symbol"],

                    trade_result["quantity"]

                )



        return trade_result