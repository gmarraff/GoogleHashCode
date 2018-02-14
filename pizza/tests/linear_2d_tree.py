import unittest
from model import Linear2DSlice
from model import Pizza
from strategy import Linear2DTree
from collections import deque

class TestLinear2DTree(unittest.TestCase):
    def get_pizza_mock():
        return Pizza(3, 5, 1, 6, ["MMMMM", "MTTTM", "MMMMM"])

    def test_algorithm(self):
        pass

    def test_big_slice(self):
        Linear2DSlice.static_init(TestLinear2DTree.get_pizza_mock())
        Linear2DTree.H, \
        Linear2DTree.L, \
        Linear2DTree.C, \
        Linear2DTree.R, \
        Linear2DTree.ROWS = \
        Linear2DSlice.pizza.h, \
        Linear2DSlice.pizza.l, \
        Linear2DSlice.pizza.c, \
        Linear2DSlice.pizza.r, \
        Linear2DSlice.pizza.rows

        excepted = deque([Linear2DSlice.create(0, 0, 3, 2), Linear2DSlice.create(0, 2, 3, 1), Linear2DSlice.create(0, 3, 3, 2)])
        test = Linear2DTree().big_slice(0, 2, 0).list
        for i in excepted:
            print("Excepted: {}".format(i))
        for i in test:
            print("Find: {}".format(i))
        self.assertEqual(test, excepted)


    def test_big_slice_solver(self):
        Linear2DSlice.static_init(TestLinear2DTree.get_pizza_mock())
        Linear2DTree.H, \
        Linear2DTree.L, \
        Linear2DTree.C, \
        Linear2DTree.R, \
        Linear2DTree.ROWS = \
        Linear2DSlice.pizza.h, \
        Linear2DSlice.pizza.l, \
        Linear2DSlice.pizza.c, \
        Linear2DSlice.pizza.r, \
        Linear2DSlice.pizza.rows
        '''
        test = Linear2DTree().big_slice_solver(0, 2, 0).list
        for i in test:
            print(i)
        '''
