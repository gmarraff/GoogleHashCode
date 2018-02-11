'''
Slice's model
'''

class LinearSlice:
    __pizza = None

    def __init__(self, r, c):
        if LinearSlice.__pizza is None:
            raise Exception("pizza not initialized with correct static method")

        self.r = int(r)
        if self.r < 0 or self.r >= LinearSlice.__pizza.r:
            raise Exception("first param (r) not in pizza's bound")

        self.c = int(c)
        if self.c < 0 or self.c >= LinearSlice.__pizza.c:
            raise Exception("second param (c) not in pizza's bound")


        self.size = 1

        self.t = 1 if LinearSlice.__pizza.rows[r][c] is 'T' else 0
        self.m = 1 if LinearSlice.__pizza.rows[r][c] is 'M' else 0


    def static_init(pizza):
        LinearSlice.__pizza = pizza

    def contain_ingredients(self):
        return \
            min(self.m, self.t) >= LinearSlice.__pizza.l and \
            self.size <= LinearSlice.__pizza.h

    def in_bound(self):
        return self.c + self.size <= LinearSlice.__pizza.c

    def not_in_bound(self):
        return not self.in_bound()

    def too_large(self, i=0):
        return self.size+i > LinearSlice.__pizza.h

    def not_too_large(self, i=0):
        return not self.too_large(i)

    def add_right(self):
        if self.size < LinearSlice.__pizza.h and self.c+self.size < LinearSlice.__pizza.c:
            self.t += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'T' else 0
            self.m += 1 if LinearSlice.__pizza.rows[self.r][self.c+self.size] is 'M' else 0
            self.size += 1
            return True
        else:
            return False

    def is_valid(self):
        return \
            self.in_bound() and \
            self.not_too_large() and \
            self.contain_ingredients()

    def is_not_valid(self):
        return not self.is_valid()

    def __str__(self):
        return "(r:{0}, c:{1}, size:{2})".format(self.r, self.c, self.size)

    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__dict__ == other.__dict__

################################################################################

import unittest
from .pizza import Pizza

class TestLinearSlice(unittest.TestCase):

    def get_default_pizza():
        return Pizza(4, 4, 1, 3, [['T', 'T', 'M', 'T'],['M', 'T', 'T', 'T'],['T', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']])

    def test_init(self):
        with self.assertRaises(Exception) as context:
            LinearSlice()
            self.assertTrue('pizza not initialized' in context.exception)
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
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
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
        slice = LinearSlice(0, 0)
        slice.add_right()
        self.assertFalse(slice.contain_ingredients())
        slice.add_right()
        self.assertTrue(slice.contain_ingredients())
        slice.size += 1
        slice.t += 1
        self.assertFalse(slice.contain_ingredients())

    def test_in_bound(self):
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
        slice = LinearSlice(0, 2)
        slice.add_right()
        self.assertTrue(slice.in_bound())
        self.assertFalse(slice.not_in_bound())
        slice.size += 1
        self.assertTrue(slice.not_in_bound())
        self.assertFalse(slice.in_bound())

    def test_too_large(self):
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
        slice = LinearSlice(0, 0)
        slice.size = 3
        self.assertFalse(slice.too_large())
        self.assertTrue(slice.not_too_large())
        slice.size = 4
        self.assertFalse(slice.not_too_large())
        self.assertTrue(slice.too_large())

    def test_add_right(self):
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
        slice = LinearSlice(0, 0)
        self.assertTrue(slice.add_right())
        self.assertTrue(slice.add_right())
        self.assertFalse(slice.add_right())
        slice = LinearSlice(0, 2)
        self.assertTrue(slice.add_right())
        self.assertFalse(slice.add_right())

    def test_equal(self):
        LinearSlice.static_init(TestLinearSlice.get_default_pizza())
        self.assertEqual(LinearSlice(0, 0), LinearSlice(0, 0))

if __name__ == '__main__':
    unittest.main()
