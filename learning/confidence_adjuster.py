class ConfidenceAdjuster:


    def __init__(self):

        self.default_multiplier = {

            "BUY": 1.0,

            "SELL": 1.0,

            "HOLD": 1.0

        }



    def calculate_adjustment(self, history):


        if not history:


            return self.default_multiplier



        results = {


            "BUY": [],

            "SELL": [],

            "HOLD": []

        }



        for trade in history:


            action = trade.get(

                "action",

                "HOLD"

            )


            success = trade.get(

                "success",

                False

            )


            if action in results:

                results[action].append(

                    success

                )



        multipliers = {}



        for action, trades in results.items():


            if len(trades) == 0:


                multipliers[action] = 1.0


                continue



            win_rate = (

                sum(trades)

                /

                len(trades)

            )



            if win_rate >= 0.70:


                multipliers[action] = 1.15



            elif win_rate <= 0.40:


                multipliers[action] = 0.85



            else:


                multipliers[action] = 1.0



        return multipliers




    def adjust_confidence(

        self,

        action,

        confidence,

        history

    ):


        adjustments = self.calculate_adjustment(

            history

        )


        multiplier = adjustments.get(

            action,

            1.0

        )


        new_confidence = confidence * multiplier



        if new_confidence > 100:

            new_confidence = 100



        return round(

            new_confidence,

            2

        )