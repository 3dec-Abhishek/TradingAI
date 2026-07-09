import yfinance as yf


class MarketDataProvider:


    def get_price_history(
            self,
            symbol,
            period="6mo"
        ):

        data = yf.download(
            symbol,
            period=period,
            auto_adjust=True,
            progress=False
        )

        # Fix yfinance multi-index columns
        if hasattr(data.columns, "levels"):
            data.columns = data.columns.get_level_values(0)

        return data



    def get_current_price(
            self,
            symbol
        ):

        ticker = yf.Ticker(symbol)

        price = (
            ticker
            .history(period="1d")
            ["Close"]
            .iloc[-1]
        )

        return float(price)