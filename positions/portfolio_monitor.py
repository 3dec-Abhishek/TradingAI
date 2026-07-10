from positions.pnl_calculator import PnLCalculator


class PortfolioMonitor:

    def __init__(

        self,

        position_manager

    ):

        self.position_manager = position_manager

    ##################################################

    def monitor(

        self,

        latest_prices

    ):

        report = []

        positions = (

            self.position_manager

            .get_open_positions()

        )

        for position in positions:

            symbol = position.symbol

            if symbol not in latest_prices:

                continue

            current_price = latest_prices[symbol]

            position.update_price(

                current_price

            )

            pnl = (

                PnLCalculator

                .calculate(position)

            )

            action = "HOLD"

            if (

                position.stop_loss is not None

                and

                current_price <= position.stop_loss

            ):

                action = "STOP LOSS"

                self.position_manager.close_position(

                    position.id

                )

            elif (

                position.take_profit is not None

                and

                current_price >= position.take_profit

            ):

                action = "TAKE PROFIT"

                self.position_manager.close_position(

                    position.id

                )

            report.append(

                {

                    "symbol": position.symbol,

                    "price": current_price,

                    "status": position.status,

                    "action": action,

                    "pnl": pnl,

                }

            )

        self.position_manager.save()

        return report