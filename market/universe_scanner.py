class UniverseScanner:


    def __init__(self):

        self.default_symbols = [

            "AAPL",
            "MSFT",
            "NVDA",
            "GOOGL",
            "AMZN",
            "META",
            "TSLA",
            "AMD",
            "SPY",
            "QQQ"

        ]



    def get_universe(
        self
    ):

        return self.default_symbols



    def add_symbol(
        self,
        symbol
    ):

        if symbol not in self.default_symbols:

            self.default_symbols.append(
                symbol
            )


        return self.default_symbols