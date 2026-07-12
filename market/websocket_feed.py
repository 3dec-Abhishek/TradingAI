import asyncio



class MarketStream:



    def __init__(self):

        self.price={}



    async def connect(
        self
    ):


        while True:


            print(
                "Streaming market data..."
            )


            await asyncio.sleep(
                1
            )



    def get_price(
        self,
        symbol
    ):


        return self.price.get(
            symbol,
            0
        )