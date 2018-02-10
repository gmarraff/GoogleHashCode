import abc
from .pizza import Pizza
from .slice import Slice

class Engine(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def algorithm(self, pizza: Pizza) -> [Slice]:
        # implements the cut algorithm
        # Args:
        #   pizza
        # Return:
        #   collection of Slice's
        pass
