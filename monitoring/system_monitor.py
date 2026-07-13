from monitoring.health_checker import HealthChecker
from monitoring.alert_manager import AlertManager



class SystemMonitor:


    def __init__(self):

        self.health=HealthChecker()

        self.alert=AlertManager()



    def run(self):


        status=self.health.check()


        failed=[

            k for k,v in status.items()

            if v!="OK"

        ]


        if failed:

            self.alert.send(

                str(failed)

            )


        return status