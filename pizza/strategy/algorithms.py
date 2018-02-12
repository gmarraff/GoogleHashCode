from .engine import Engine
from model import Pizza
from model import LinearSlice
from model import AntiLinearSlice

class Linear(Engine):

    def algorithm(self, pizza):
        LinearSlice.static_init(pizza)
        out = []
        anti = []
        for i in range(0, pizza.r):
            call = self.linear(i, pizza.c)
            out.append(call[0])
            anti.append(call[1])
        # TODO: other stuff
        return [item for sublist in out for item in sublist]

    def linear(self, index, max):
        array_slices = []
        array_anti = []
        i = 0
        while i < max:
            slice, anti, i = self.add_slice(index, i)
            if slice is not None:
                array_slices.append(slice)
            elif anti is not None and len(array_anti) > 1 and array_anti[-1].c is i - 2:
                array_anti[-1].add_right()
            else:
                array_anti.append(anti)

        return array_slices, array_anti

    def add_slice(self, i, j):
        slice = LinearSlice(i, j)
        counter = j + 1
        while \
            slice.is_not_valid() and \
            slice.add_right():
            counter += 1
        if slice.is_valid():
            return slice, None, counter
        else:
            return None, AntiLinearSlice(i, j), j + 1
