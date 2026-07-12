from abc import ABC, abstractmethod



class BrokerInterface(ABC):


    @abstractmethod
    def buy(
        self,
        symbol,
        quantity
    ):

        pass



    @abstractmethod
    def sell(
        self,
        symbol,
        quantity
    ):

        pass



    @abstractmethod
    def account(self):

        pass
