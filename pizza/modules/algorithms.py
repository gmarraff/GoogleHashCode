from .engine import Engine
from .pizza import Pizza
from .slice import Slice

class Linear(Engine):

    def algorithm(self, pizza: Pizza) -> [Slice]:
        #Matrix = [linear(row) for row in pizza.rows]
        print ("tajo")
