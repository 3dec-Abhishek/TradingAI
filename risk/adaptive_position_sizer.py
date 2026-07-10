class AdaptivePositionSizer:

    def __init__(self):

        self.max_portfolio_risk = 0.02
        self.max_position_size = 0.10
        self.min_position_size = 0.01

    def calculate(

        self,

        portfolio_value,

        price,

        confidence,

        regime,

        risk_status

    ):

        confidence = max(0, min(confidence, 100))

        # Base allocation (5%)
        allocation = 0.05

        # Confidence adjustment
        allocation *= (confidence / 50)

        # Market regime adjustment
        if regime == "BULLISH":
            allocation *= 1.25

        elif regime == "BEARISH":
            allocation *= 0.60

        elif regime == "SIDEWAYS":
            allocation *= 0.80

        elif regime == "HIGH_VOLATILITY":
            allocation *= 0.50

        # Risk adjustment
        if str(risk_status).upper() in ["FAIL", "FAILED", "REJECTED"]:
            allocation *= 0.25

        allocation = max(
            self.min_position_size,
            min(
                allocation,
                self.max_position_size
            )
        )

        dollars = portfolio_value * allocation

        quantity = int(dollars / price)

        if quantity < 1:
            quantity = 1

        return {

            "allocation": round(allocation * 100, 2),

            "position_value": round(quantity * price, 2),

            "quantity": quantity,

            "price": price

        }