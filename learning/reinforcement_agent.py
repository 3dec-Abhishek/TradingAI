class ReinforcementAgent:



    def learn(
        self,
        memory
    ):


        if len(memory)==0:

            return {


                "status":

                "NO_DATA"

            }



        rewards=[

            x["reward"]

            for x in memory

        ]



        average=sum(rewards)/len(rewards)



        return {


            "learning_score":

            round(
                average,
                3
            ),


            "samples":

            len(memory)

        }