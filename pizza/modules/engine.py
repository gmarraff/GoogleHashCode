import abc
from .pizza import Pizza
from .slice import LinearSlice

class Engine(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def algorithm(self, pizza):
        # implements the cut algorithm
        # Args:
        #   pizza
        # Return:
        #   collection of Slice's
        pass
