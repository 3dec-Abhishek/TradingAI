class UniverseManager:

    def __init__(self):

        self.symbols = [

            "AAPL",
            "MSFT",
            "NVDA",
            "AMZN",
            "GOOGL",
            "META",
            "TSLA",
            "AMD",
            "SPY",
            "QQQ"

        ]

    def get_symbols(self):

        return self.symbols

    def add_symbol(self, symbol):

        if symbol not in self.symbols:

            self.symbols.append(symbol)

    def remove_symbol(self, symbol):

        if symbol in self.symbols:

            self.symbols.remove(symbol)