class PositionManager:


    def __init__(self):

        self.max_position = 20


    def evaluate(
        self,
        positions,
        market,
        decision
    ):


        symbol = market.get(
            "symbol"
        )


        result = {

            "action":"HOLD",

            "reason":[]

        }



        if symbol not in positions:

            result["action"]="NEW"

            result["reason"].append(
                "No existing position"
            )

            return result



        position = positions[symbol]


        quantity = position.get(
            "quantity",
            0
        )


        avg_price = position.get(
            "average_price",
            0
        )


        current = market.get(
            "price",
            0
        )


        gain = (
            (current-avg_price)
            /
            avg_price
        )*100



        if gain > 20:


            result["action"]="REDUCE"

            result["reason"].append(
                "Profit target reached"
            )


        elif gain < -10:


            result["action"]="EXIT"

            result["reason"].append(
                "Stop loss triggered"
            )


        else:


            result["action"]="HOLD"

            result["reason"].append(
                "Position healthy"
            )


        return result