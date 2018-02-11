import unittest
from model import Pizza
from model import LinearSlice

class TestLinearSlice(unittest.TestCase):

    def get_pizza_mock():
        return Pizza(4, 4, 1, 3, [['T', 'T', 'M', 'T'],['M', 'T', 'T', 'T'],['T', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']])

    def test_init(self):
        with self.assertRaises(Exception) as context:
            LinearSlice()
            self.assertTrue('pizza not initialized' in context.exception)
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        with self.assertRaises(Exception) as context:
            LinearSlice(-1, 0)
            self.assertTrue('first param (r)' in context.exception)
            LinearSlice(4, 0)
            self.assertTrue('first param (r)' in context.exception)
        with self.assertRaises(Exception) as context:
            LinearSlice(0, -1)
            self.assertTrue('second param (c)' in context.exception)
            LinearSlice(0, 4)
            self.assertTrue('second param (c)' in context.exception)
        self.assertEqual(LinearSlice(0, 0).t, 1)
        self.assertEqual(LinearSlice(1, 0).m, 1)

    def test_contain_ingredients(self):
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        slice = LinearSlice(0, 0)
        slice.add_right()
        self.assertFalse(slice.contain_ingredients())
        slice.add_right()
        self.assertTrue(slice.contain_ingredients())
        slice.size += 1
        slice.t += 1
        self.assertFalse(slice.contain_ingredients())

    def test_in_bound(self):
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        slice = LinearSlice(0, 2)
        slice.add_right()
        self.assertTrue(slice.in_bound())
        self.assertFalse(slice.not_in_bound())
        slice.size += 1
        self.assertTrue(slice.not_in_bound())
        self.assertFalse(slice.in_bound())

    def test_too_large(self):
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        slice = LinearSlice(0, 0)
        slice.size = 3
        self.assertFalse(slice.too_large())
        self.assertTrue(slice.not_too_large())
        slice.size = 4
        self.assertFalse(slice.not_too_large())
        self.assertTrue(slice.too_large())

    def test_add_right(self):
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        slice = LinearSlice(0, 0)
        self.assertTrue(slice.add_right())
        self.assertTrue(slice.add_right())
        self.assertFalse(slice.add_right())
        slice = LinearSlice(0, 2)
        self.assertTrue(slice.add_right())
        self.assertFalse(slice.add_right())

    def test_equal(self):
        LinearSlice.static_init(TestLinearSlice.get_pizza_mock())
        self.assertEqual(LinearSlice(0, 0), LinearSlice(0, 0))
