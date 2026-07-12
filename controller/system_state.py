class SystemState:


    def __init__(self):

        self.state={

            "running":False,

            "cycles":0,

            "last_action":None,

            "errors":0

        }



    def update_cycle(self):

        self.state["cycles"] +=1



    def set_action(self,action):

        self.state["last_action"]=action



    def error(self):

        self.state["errors"]+=1



    def get(self):

        return self.state