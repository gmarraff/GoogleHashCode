from .engine import Engine
from model import Pizza
from model import LinearSlice

class Linear(Engine):

    def algorithm(self, pizza):
        LinearSlice.static_init(pizza)
        out = []
        for i in range(0, pizza.r):
            out.append(self.linear(i, pizza.c))
        # TODO: other stuff
        return out

    def linear(self, index, max):
        array_slices = []
        i = 0
        while i < max:
            slice, i = self.add_slice(index, i)
            if slice is not None:
                array_slices.append(slice)
        return array_slices

    def add_slice(self, i, j):
        slice = LinearSlice(i, j)
        counter = j + 1
        while \
            slice.is_not_valid() and \
            slice.add_right():
            counter += 1
        if slice.is_valid():
            return slice, counter
        elif slice.too_large(1):
            return self.add_slice(i, j+1)
        else:
            return None, counter
