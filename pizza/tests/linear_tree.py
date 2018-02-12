import unittest
from model import LinearSlice
from model import Pizza
from strategy import LinearTree

class TestLinearTree(unittest.TestCase):
    def get_pizza_mock():
        return Pizza(1, 14, 2, 7, ["TTMTMMMMMMMTTM"])

    def test_algorithm(self):
        pass

    def test_tree_row(self):
        LinearSlice.static_init(TestLinearTree.get_pizza_mock())
        self.assertEqual(LinearTree().tree_row(0)[1], 14)

    def test_add_slice(self):
        LinearSlice.static_init(TestLinearTree.get_pizza_mock())
        test = LinearSlice(0, 0)
        test.add_right()
        test.add_right()
        test.add_right()
        test.add_right()
        self.assertIsNone(LinearTree().add_slice(0, 0))
        self.assertIsNone(LinearTree().add_slice(0, 1))
        self.assertIsNone(LinearTree().add_slice(0, 2))
        self.assertIsNone(LinearTree().add_slice(0, 3))
        self.assertIsNone(LinearTree().add_slice(0, 4))
        self.assertEqual(LinearTree().add_slice(0, 5), test)
        test.add_right()
        self.assertEqual(LinearTree().add_slice(0, 6), test)
        test.add_right()
        self.assertEqual(LinearTree().add_slice(0, 7), test)
        self.assertIsNone(LinearTree().add_slice(0, 8))
