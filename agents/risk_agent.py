class RiskAgent:

    def analyze(
        self,
        portfolio,
        proposed_trade
    ):

        # =========================
        # Extract Portfolio Value
        # =========================

        portfolio_value = (
            portfolio
            .get("account", {})
            .get("portfolio_value")
        )


        if portfolio_value is None:
            raise ValueError(
                "Portfolio value missing from portfolio data"
            )


        # =========================
        # Trade Data
        # =========================

        trade_size = proposed_trade.get(
            "trade_size",
            0
        )

        options_value = proposed_trade.get(
            "options_value",
            0
        )

        today_loss = proposed_trade.get(
            "today_loss",
            0
        )


        results = {}


        # =========================
        # Position Size Risk
        # =========================

        position_percentage = (
            trade_size /
            portfolio_value
        ) * 100


        results["position_size"] = {

            "value": round(
                position_percentage,
                2
            ),

            "limit": 10,

            "status":
                "PASS"
                if position_percentage <= 10
                else "FAIL"
        }



        # =========================
        # Options Exposure Risk
        # =========================

        options_percentage = (
            options_value /
            portfolio_value
        ) * 100


        results["options_exposure"] = {

            "value": round(
                options_percentage,
                2
            ),

            "limit": 20,

            "status":
                "PASS"
                if options_percentage <= 20
                else "FAIL"
        }



        # =========================
        # Daily Loss Risk
        # =========================

        loss_percentage = (
            today_loss /
            portfolio_value
        ) * 100


        results["daily_loss"] = {

            "value": round(
                loss_percentage,
                2
            ),

            "limit": 2,

            "status":
                "PASS"
                if loss_percentage <= 2
                else "FAIL"
        }



        # =========================
        # Final Decision
        # =========================

        failed_checks = [

            check
            for check in results.values()

            if check["status"] == "FAIL"

        ]


        results["trade_status"] = (

            "APPROVED"

            if len(failed_checks) == 0

            else "REJECTED"

        )


        return results