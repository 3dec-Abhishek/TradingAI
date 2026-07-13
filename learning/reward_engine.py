class RewardEngine:


    def calculate(
        self,
        trade
    ):


        pnl = trade.get(
            "pnl",
            0
        )


        if pnl > 0:

            reward = 1


        elif pnl < 0:

            reward = -1


        else:

            reward = 0



        return {


            "reward":

            reward,


            "pnl":

            pnl

        }