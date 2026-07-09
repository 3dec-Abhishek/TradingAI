class TradeValidator:

    def validate(
        self,
        position_size,
        max_position,
        exposure_ok,
        loss_ok,
    ):

        approved = (

            position_size <= max_position

            and exposure_ok

            and loss_ok

        )

        return {

            "approved": approved,

            "checks": {

                "position_size": position_size <= max_position,

                "options_exposure": exposure_ok,

                "daily_loss": loss_ok,

            }

        }