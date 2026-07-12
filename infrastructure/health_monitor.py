class HealthMonitor:


    def __init__(self):

        self.components={}



    def register(
        self,
        name,
        status
    ):

        self.components[name]=status



    def check(self):

        return self.components