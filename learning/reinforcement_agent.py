class ReinforcementAgent:



    def __init__(self):

        self.q_table={}



    def update(
        self,
        state,
        action,
        reward
    ):


        key=(state,action)


        old=self.q_table.get(
            key,
            0
        )


        self.q_table[key]= (

            old*0.8
            +
            reward*0.2

        )



    def best_action(
        self,
        state
    ):


        choices={}


        for (
            s,a
        ),value in self.q_table.items():


            if s==state:

                choices[a]=value



        if not choices:

            return "HOLD"



        return max(

            choices,

            key=choices.get

        )