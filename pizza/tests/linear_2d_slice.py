import unittest
from model import Linear2DSlice
from model import Pizza

class TestLinear2DSlice(unittest.TestCase):
    def get_pizza_mock():
        return Pizza(3, 14, 2, 7, ["TTMTMMMMTMMTTM", "TTMTMMTMMMMTTM", "TTMTMMMMTMMTTM"])

    def test_init(self):

        pass

    def test_static_init(self):
        with self.assertRaises(Exception) as context:
            Linear2DSlice(0, 0, 0, 0)
        self.assertTrue('pizza not initialized' in str(context.exception))
        Linear2DSlice.static_init(TestLinear2DSlice.get_pizza_mock())
        slice = Linear2DSlice.create(0, 0, 3, 4)
