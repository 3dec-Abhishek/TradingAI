class ExecutionSafety:


    def validate(
        self,
        decision,
        portfolio
    ):


        if decision["quantity"] <=0:

            return False


        if decision["confidence"] <60:

            return False


        return True