class SystemValidator:


    def __init__(self):
        self.errors = []



    def check(self, engine):

        self.errors = []


        required = [

            "broker",
            "market_agent",
            "strategy_agent",
            "risk_agent",
            "decision_agent",
            "execution_manager",
            "learning_engine"

        ]


        for item in required:

            if not hasattr(engine, item):

                self.errors.append(
                    f"Missing component: {item}"
                )


        return {

            "status":
                "OK"
                if len(self.errors)==0
                else "FAILED",

            "errors":
                self.errors

        }