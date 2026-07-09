from abc import ABC, abstractmethod


class BaseStrategy(ABC):


    @abstractmethod
    def analyze(self, market_data):
        pass
