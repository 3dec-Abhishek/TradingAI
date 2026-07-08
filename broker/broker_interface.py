from abc import ABC, abstractmethod


class BrokerInterface(ABC):

    @abstractmethod
    def get_account(self):
        pass


    @abstractmethod
    def get_positions(self):
        pass
