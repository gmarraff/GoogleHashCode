from .engine import Engine

class Solver:

    def __init__(self, strategy):
        self.strategy = strategy

    def cut(self, pizza):
        return self.strategy.algorithm(pizza)

    def changeAlgorithm(self, newAlgorithm):
        self.strategy = newAlgorithm
