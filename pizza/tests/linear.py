import unittest
from model import LinearSlice
from model import Pizza
from strategy import Linear

class TestLinear(unittest.TestCase):
    def get_pizza_mock():
        return Pizza(4, 4, 1, 3, [['T', 'T', 'M', 'T'],['M', 'T', 'M', 'T'],['T', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']])

    def test_algorithm(self):
        pass

    def test_linear(self):
        '''
        LinearSlice.static_init(TestLinear.get_pizza_mock())
        test = LinearSlice(0, 0)
        test.add_right()
        test.add_right()
        #self.assertEqual(Linear().linear(0, 4), [test])
        test = LinearSlice(1, 0)
        test.add_right()
        test1 = LinearSlice(1, 2)
        test1.add_right()
        self.assertEqual(Linear().linear(1, 4), [test, test1])
        self.assertEqual(Linear().linear(2, 4), [])
        '''
        pass

    def test_add_slice(self):
        '''
        LinearSlice.static_init(TestLinear.get_pizza_mock())
        test = LinearSlice(0, 0)
        test.add_right()
        test.add_right()
        self.assertEqual(Linear().add_slice(0, 0)[0], test)
        self.assertEqual(Linear().add_slice(0, 0)[1], 3)
        self.assertIsNone(Linear().add_slice(2, 0)[0])
        self.assertEqual(Linear().add_slice(2, 0)[1], 4)
        self.assertIsNone(Linear().add_slice(0, 3)[0])
        self.assertEqual(Linear().add_slice(0, 3)[1], 4)
        '''
        pass
