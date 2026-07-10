class OpportunityRanker:

    def __init__(self):

        self.weights = {

            "trend": 0.30,

            "rsi": 0.20,

            "confidence": 0.25,

            "regime": 0.15,

            "risk": 0.10

        }

    def score(self, market, signals, decision, regime):

        score = 0

        # Trend

        sma20 = market.get("20_day_sma", market.get("sma20", 0))
        sma50 = market.get("50_day_sma", market.get("sma50", 0))
        price = market.get("price", 0)

        if price > sma20 > sma50:

            score += 30

        # RSI

        rsi = market.get("rsi", 50)

        if 45 <= rsi <= 65:

            score += 20

        elif 30 <= rsi < 45:

            score += 15

        elif 65 < rsi <= 75:

            score += 10

        # Decision confidence

        score += decision.get("confidence", 50) * 0.25

        # Market regime

        if regime.get("regime") == "BULLISH":

            score += 15

        elif regime.get("regime") == "SIDEWAYS":

            score += 8

        elif regime.get("regime") == "BEARISH":

            score -= 10

        elif regime.get("regime") == "HIGH_VOLATILITY":

            score -= 15

        return round(score, 2)

    def rank(self, opportunities):

        ranked = sorted(

            opportunities,

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked