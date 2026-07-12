class HealthMonitor:


    def check(self,engine):


        status={}



        try:

            status["broker"]="OK"

        except:

            status["broker"]="FAILED"



        try:

            status["market"]="OK"

        except:

            status["market"]="FAILED"



        try:

            status["ai"]="OK"

        except:

            status["ai"]="FAILED"



        return status