from risk.config import MAX_OPTIONS_EXPOSURE


class ExposureChecker:

    def check(
        self,
        options_value,
        portfolio_value,
    ):

        exposure = (
            options_value /
            portfolio_value
        )

        return {
            "current": exposure,
            "allowed": MAX_OPTIONS_EXPOSURE,
            "approved": exposure <= MAX_OPTIONS_EXPOSURE,
        }