class BackTester:


    def __init__(self):

        self.results=[]



    def run(
        self,
        historical_data,
        strategy
    ):


        capital=10000

        trades=0

        wins=0



        for candle in historical_data:


            signal = strategy.analyze(
                candle
            )


            if signal=="BUY":

                trades+=1

                result = self.simulate_trade(
                    candle
                )


                if result>0:

                    wins+=1


                capital += result



        return {


            "starting_capital":10000,


            "ending_capital":capital,


            "trades":trades,


            "win_rate":

                (
                    wins/trades*100
                )
                if trades else 0


        }



    def simulate_trade(
        self,
        candle
    ):


        entry=candle["open"]

        exit=candle["close"]


        return exit-entry