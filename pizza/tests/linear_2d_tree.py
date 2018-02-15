import unittest
from model import Linear2DSlice
from model import Pizza
from strategy import Linear2DTree
from collections import deque
from modules import validate
from strategy import Solver

class TestLinear2DTree(unittest.TestCase):
    def get_pizza_mock():
        return Pizza(6, 7, 1, 5, ["TMMMTTT", "MMMMTMM", "TTMTTMT", "TMMTMMM", "TTTTTTM", "TTTTTTM"])

    def test_algorithm(self):
        solver = Solver(Linear2DTree())
        Linear2DTree.resize_pizza(1)
        Linear2DTree.perc(1.0)
        test = solver.cut(TestLinear2DTree.get_pizza_mock())
        score = sum([slice.score for slice in test])
        for i in test: print(i)
        self.assertEqual(score, 42)
        self.assertTrue(validate(test))

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

        self.assertEqual(Linear2DTree().big_slice(0, 5, 0, 6).score, 42)
        self.assertTrue(validate(Linear2DTree().big_slice(0, 5, 0, 6).list))


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

        pass
