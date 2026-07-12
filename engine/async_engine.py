import asyncio



class AsyncTradingEngine:



    def __init__(
        self,
        engine
    ):

        self.engine = engine



    async def market_worker(
        self
    ):


        while True:


            self.engine.market_agent.analyze(
                "AAPL"
            )


            await asyncio.sleep(
                5
            )



    async def trading_worker(
        self
    ):


        while True:


            self.engine.run()


            await asyncio.sleep(
                60
            )



    async def start(
        self
    ):


        await asyncio.gather(

            self.market_worker(),

            self.trading_worker()

        )