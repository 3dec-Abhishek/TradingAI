from broker.broker_interface import BrokerInterface


class MockBroker(BrokerInterface):

    def get_account(self):

        return {
            "cash": 5000,
            "portfolio_value": 25000
        }


    def get_positions(self):

        return [
            {
                "symbol": "AAPL",
                "quantity": 20,
                "value": 4000,
                "gain_percent": 12.4
            },

            {
                "symbol": "TSLA",
                "quantity": 5,
                "value": 3000,
                "gain_percent": -8.1
            }
        ]
