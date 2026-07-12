class IntelligenceEngine:


    def __init__(self):

        self.history = []



    def evaluate(
        self,
        opportunities
    ):


        if not opportunities:

            return None



        ranked = sorted(

            opportunities,

            key=lambda x:
            x.get(
                "score",
                0
            ),

            reverse=True

        )


        best = ranked[0]


        self.history.append(
            best
        )


        return best