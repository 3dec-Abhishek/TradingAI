from risk.position_sizing import PositionSizer
from risk.exposure import ExposureChecker
from risk.daily_loss import DailyLossChecker
from risk.trade_validator import TradeValidator


class RiskEngine:

    def __init__(self):

        self.position = PositionSizer()

        self.exposure = ExposureChecker()

        self.loss = DailyLossChecker()

        self.validator = TradeValidator()

    def analyze(

        self,

        portfolio_value,

        trade_size,

        options_value,

        today_loss,

    ):

        max_position = (

            self.position.calculate(

                portfolio_value

            )

        )

        exposure = (

            self.exposure.check(

                options_value,

                portfolio_value,

            )

        )

        loss = (

            self.loss.check(

                portfolio_value,

                today_loss,

            )

        )

        return self.validator.validate(

            trade_size,

            max_position,

            exposure["approved"],

            loss["approved"],

        )