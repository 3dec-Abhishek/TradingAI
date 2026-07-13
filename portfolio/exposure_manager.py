class ExposureManager:

    def analyze(self, portfolio):

        total = portfolio["portfolio_value"]

        exposures=[]

        for symbol,data in portfolio["positions"].items():

            exposure=data["market_value"]/total

            exposures.append({

                "symbol":symbol,

                "exposure":round(exposure*100,2)

            })

        return exposures