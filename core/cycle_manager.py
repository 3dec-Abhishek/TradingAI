class CycleManager:


    def __init__(self):

        self.cycle=0



    def start(self):

        self.cycle +=1


        print(
            "\nTRADING CYCLE:",
            self.cycle
        )


        return self.cycle