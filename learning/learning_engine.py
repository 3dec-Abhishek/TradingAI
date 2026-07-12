class LearningEngine:

    def __init__(

        self,

        tracker,

        strategy_tracker

    ):

        self.tracker = tracker

        self.strategy_tracker = strategy_tracker

    ##################################################

    def generate_feedback(self):

        report = self.strategy_tracker.analyze()

        feedback = []

        if len(report) == 0:

            feedback.append(
                "No historical trades available."
            )

            return feedback

        for strategy, stats in report.items():

            if stats["win_rate"] >= 70:

                feedback.append(

                    f"{strategy}: Excellent strategy "
                    f"({stats['win_rate']}% win rate). "
                    f"Consider increasing allocation."

                )

            elif stats["win_rate"] >= 55:

                feedback.append(

                    f"{strategy}: Performing well "
                    f"({stats['win_rate']}% win rate)."

                )

            elif stats["win_rate"] >= 40:

                feedback.append(

                    f"{strategy}: Average performance "
                    f"({stats['win_rate']}%). "
                    f"Needs optimization."

                )

            else:

                feedback.append(

                    f"{strategy}: Poor performance "
                    f"({stats['win_rate']}%). "
                    f"Reduce usage."

                )

        return feedback
    
    def recommend_strategy(self, performance):
        if performance["win_rate"] > 60:

            return "INCREASE"

        elif performance["win_rate"] < 40:
            return "DECREASE"
    

        return "MAINTAIN"