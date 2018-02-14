from .engine import Engine
from modules import time_track

class Solver:

    def __init__(self, strategy):
        self.strategy = strategy

    @time_track
    def cut(self, pizza):
        return self.strategy.algorithm(pizza)

    def changeAlgorithm(self, newAlgorithm):
        self.strategy = newAlgorithm
