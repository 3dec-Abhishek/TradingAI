class AgentManager:



    def __init__(self):

        self.agents={}



    def register(
        self,
        name,
        agent
    ):


        self.agents[name]=agent



    def send(
        self,
        agent,
        message
    ):


        return self.agents[agent].analyze(
            message
        )