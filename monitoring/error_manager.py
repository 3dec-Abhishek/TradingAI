class ErrorManager:


    def __init__(self):

        self.errors=[]



    def record(self,error):

        self.errors.append({

            "error":str(error)

        })



    def report(self):

        return self.errors