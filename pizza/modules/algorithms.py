from .engine import Engine
from .pizza import Pizza
from .slice import LinearSlice

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

################################################################################

import unittest

class TestLinear(unittest.TestCase):
    def get_default_pizza():
        return Pizza(4, 4, 1, 3, [['T', 'T', 'M', 'T'],['M', 'T', 'M', 'T'],['T', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']])

    def test_algorithm(self):
        pass

    def test_linear(self):
        LinearSlice.static_init(TestLinear.get_default_pizza())
        test = LinearSlice(0, 0)
        test.add_right()
        test.add_right()
        self.assertEqual(Linear().linear(0, 4), [test])
        test = LinearSlice(1, 0)
        test.add_right()
        test1 = LinearSlice(1, 2)
        test1.add_right()
        self.assertEqual(Linear().linear(1, 4), [test, test1])
        self.assertEqual(Linear().linear(2, 4), [])

    def test_add_slice(self):
        LinearSlice.static_init(TestLinear.get_default_pizza())
        test = LinearSlice(0, 0)
        test.add_right()
        test.add_right()
        self.assertEqual(Linear().add_slice(0, 0)[0], test)
        self.assertEqual(Linear().add_slice(0, 0)[1], 3)
        self.assertIsNone(Linear().add_slice(2, 0)[0])
        self.assertEqual(Linear().add_slice(2, 0)[1], 4)
        self.assertIsNone(Linear().add_slice(0, 3)[0])
        self.assertEqual(Linear().add_slice(0, 3)[1], 4)


if __name__ == '__main__':
    unittest.main()
