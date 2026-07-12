class OpportunityScanner:


    def __init__(
        self,
        market_agent,
        strategy_agent,
        regime_detector
    ):

        self.market_agent = market_agent

        self.strategy_agent = strategy_agent

        self.regime_detector = regime_detector



    def scan(
        self,
        symbols
    ):


        opportunities = []



        for symbol in symbols:


            try:


                market = (
                    self.market_agent.analyze(
                        symbol
                    )
                )


                signals = (
                    self.strategy_agent.analyze(
                        market
                    )
                )


                regime = (
                    self.regime_detector.analyze(
                        market
                    )
                )


                score = self.calculate_score(

                    market,

                    signals,

                    regime

                )



                opportunities.append({

                    "symbol":
                    symbol,


                    "market":
                    market,


                    "signal":
                    signals,


                    "regime":
                    regime,


                    "score":
                    score

                })


            except Exception as e:


                print(
                    "Scanner Error",
                    symbol,
                    e
                )



        return sorted(

            opportunities,

            key=lambda x:
            x["score"],

            reverse=True

        )



    def calculate_score(
        self,
        market,
        signals,
        regime
    ):


        score = 0



        # Strategy confidence

        score += (
            signals.get(
                "confidence",
                50
            )
            *
            0.4
        )



        # RSI

        rsi = market.get(
            "rsi",
            50
        )


        if 40 < rsi < 70:

            score += 20



        # Trend

        if market.get(
            "trend"
        ) == "BULLISH":

            score += 20



        # Regime

        if regime.get(
            "regime"
        ) == "BULLISH":

            score += 20



        return round(
            score,
            2
        )