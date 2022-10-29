from abc import ABC, abstractmethod


class WriteStrategy(ABC):

    @abstractmethod
    def writeBehaviour(self):
        pass


