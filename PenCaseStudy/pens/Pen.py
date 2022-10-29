from abc import  ABC, abstractmethod


class Pen(ABC):

    @property
    def name(self):
        return self.name

    @property
    def cap(self):
        return self.cap

    @property
    def brand(self):
        return self.brand

    @property
    def length(self):
        return self.length

    @property
    def write_strategy(self):
        return self.write_strategy

    @abstractmethod
    def write(self):
        pass

