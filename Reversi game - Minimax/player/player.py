from abc import ABC, abstractmethod

class PlayerInterface(ABC):
    
    @property
    def symbol(self):
        return self._symbol
    
    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @abstractmethod
    def make_move():
        pass
