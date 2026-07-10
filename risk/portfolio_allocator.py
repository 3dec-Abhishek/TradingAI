class PortfolioAllocator:

    def __init__(self):

        self.max_single_position = 0.20      # 20%
        self.max_sector_exposure = 0.40      # 40%
        self.min_cash = 0.10                 # Keep 10% cash

    def allocate(
        self,
        portfolio,
        decision,
        position_size
    ):

        portfolio_value = portfolio.get(
            "portfolio_value",
            0
        )

        cash = portfolio.get(
            "cash",
            0
        )

        current_positions = portfolio.get(
            "positions",
            {}
        )

        new_value = position_size.get(
            "position_value",
            0
        )

        cash_after_trade = cash - new_value

        cash_ratio = (
            cash_after_trade / portfolio_value
            if portfolio_value > 0 else 0
        )

        approved = True
        reasons = []

        if cash_ratio < self.min_cash:

            approved = False

            reasons.append(
                "Cash reserve would fall below minimum."
            )

        allocation = (
            new_value / portfolio_value
            if portfolio_value > 0 else 0
        )

        if allocation > self.max_single_position:

            approved = False

            reasons.append(
                "Single position exceeds maximum allocation."
            )

        return {

            "approved": approved,

            "allocation": round(allocation * 100, 2),

            "cash_after_trade": round(cash_after_trade, 2),

            "cash_ratio": round(cash_ratio * 100, 2),

            "reasons": reasons

        }