class MasterRiskGate:


    def approve(self,decision,risk):

        if risk["status"]=="FAIL":

            return False


        if decision["confidence"] < 60:

            return False


        return True