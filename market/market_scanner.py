from market.market_agent import MarketAgent


class MarketScanner:


    def __init__(self):

        self.agent = MarketAgent()



    def scan(self, symbols):

        """
        Scan complete market universe.

        Returns:
        [
            {
                symbol,
                price,
                indicators
            }
        ]
        """

        results = []


        for symbol in symbols:

            try:

                data = self.agent.analyze(
                    symbol
                )


                if data:

                    results.append(
                        data
                    )


            except Exception as e:

                print(
                    "Market Scanner Error:",
                    symbol,
                    e
                )


        return results