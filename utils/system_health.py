# utils/system_health.py


class SystemHealth:


    def __init__(self, engine):

        self.engine = engine



    def check(self):

        status = {}


        # Broker

        try:

            if self.engine.broker:

                status["broker"] = "OK"

            else:

                status["broker"] = "FAILED"


        except Exception:

            status["broker"] = "FAILED"



        # Market Agent

        try:

            if self.engine.market_agent:

                status["market"] = "OK"

            else:

                status["market"] = "FAILED"


        except Exception:

            status["market"] = "FAILED"



        # AI

        try:

            if self.engine.ai_agent:

                status["ai"] = "OK"

            else:

                status["ai"] = "NOT LOADED"


        except Exception:

            status["ai"] = "FAILED"



        # Learning

        try:

            if self.engine.learning_engine:

                status["learning"] = "OK"

            else:

                status["learning"] = "FAILED"


        except Exception:

            status["learning"] = "FAILED"



        return status



    def display(self):


        print("\n")
        print("=" * 60)
        print("SYSTEM HEALTH CHECK")
        print("=" * 60)


        health = self.check()


        for key, value in health.items():

            print(
                f"{key.upper():15}: {value}"
            )


        print("=" * 60)


        return health