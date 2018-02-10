from .engine import Engine
from .pizza import Pizza
from .slice import Slice

class Solver:

    def __init__(self, strategy: Engine):
        self.strategy = strategy

    def cut(self, pizza: Pizza) -> [Slice]:
        return self.strategy.algorithm(pizza)

    def changeAlgorithm(self, newAlgorithm: Engine) -> None:
        self.strategy = newAlgorithm
