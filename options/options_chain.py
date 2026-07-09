class OptionsChain:


    def get_chain(self, symbol, price):


        return [

            {
                "symbol": symbol,
                "type": "CALL",
                "strike": round(price),
                "premium": 2.20,
                "days": 30
            },


            {
                "symbol": symbol,
                "type": "CALL",
                "strike": round(price + 10),
                "premium": 1.10,
                "days": 30
            },


            {
                "symbol": symbol,
                "type": "PUT",
                "strike": round(price),
                "premium": 2.00,
                "days": 30
            }

        ]