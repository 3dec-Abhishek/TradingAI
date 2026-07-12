class TradingAIException(Exception):
    pass



class MarketDataException(
    TradingAIException
):
    pass



class ExecutionException(
    TradingAIException
):
    pass



class RiskException(
    TradingAIException
):
    pass