from learning.reward_engine import RewardEngine
from learning.policy_memory import PolicyMemory
from learning.reinforcement_agent import ReinforcementAgent



class RLEngine:



    def __init__(self):

        self.reward = RewardEngine()

        self.memory = PolicyMemory()

        self.agent = ReinforcementAgent()



    def learn(
        self,
        trade,
        state,
        action
    ):


        reward=self.reward.calculate(
            trade
        )


        self.memory.store(

            state,

            action,

            reward["reward"]

        )


        return self.agent.learn(

            self.memory.get_memory()

        )