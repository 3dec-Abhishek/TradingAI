from risk.correlation_engine import CorrelationEngine
from risk.exposure_analyzer import ExposureAnalyzer
from risk.var_engine import VaREngine
from risk.stress_tester import StressTester
from risk.risk_controller import RiskController



class AdvancedRiskEngine:



    def __init__(self):

        self.correlation = CorrelationEngine()

        self.exposure = ExposureAnalyzer()

        self.var = VaREngine()

        self.stress = StressTester()

        self.controller = RiskController()



    def analyze(
        self,
        portfolio,
        market_data
    ):


        correlation = self.correlation.analyze(
            market_data
        )


        exposure = self.exposure.analyze(
            portfolio
        )


        portfolio_value = portfolio.get(
            "portfolio_value",
            0
        )


        volatility = 0.2



        var = self.var.calculate(

            portfolio_value,

            volatility

        )


        stress = self.stress.run(

            portfolio_value

        )


        score = 100



        if correlation["status"] == "HIGH":

            score -= 15



        if var["risk_level"] == "HIGH":

            score -= 30



        decision = self.controller.evaluate(

            score

        )



        return {


            "risk_score":

            score,


            "correlation":

            correlation,


            "exposure":

            exposure,


            "var":

            var,


            "stress":

            stress,


            "control":

            decision

        }