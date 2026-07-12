class SystemHealth:


    def check(self, engine):

        status = {}


        status["broker"] = (
            engine.broker is not None
        )


        status["market"] = (
            engine.market_agent is not None
        )


        status["ai"] = (
            engine.ai_agent is not None
        )


        status["learning"] = (
            engine.learning_engine is not None
        )


        return status