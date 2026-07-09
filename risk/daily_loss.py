from risk.config import MAX_DAILY_LOSS


class DailyLossChecker:

    def check(
        self,
        portfolio_value,
        today_loss,
    ):

        limit = (
            portfolio_value *
            MAX_DAILY_LOSS
        )

        return {

            "loss": today_loss,

            "limit": limit,

            "approved": today_loss < limit,

        }