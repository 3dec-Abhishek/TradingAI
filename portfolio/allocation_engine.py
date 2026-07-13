class AllocationEngine:


    def calculate(
        self,
        portfolio_value,
        opportunities
    ):


        allocations = {}


        total_score = sum(

            x["score"]

            for x in opportunities

        )


        for item in opportunities:


            if total_score == 0:

                allocation = 0

            else:

                allocation = (

                    item["score"]

                    /

                    total_score

                    *

                    100

                )


            allocations[
                item["symbol"]
            ] = round(
                allocation,
                2
            )


        return allocations