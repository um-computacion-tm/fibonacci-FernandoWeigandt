import unittest
from fibonacci import *


class TestFibonacci(unittest.TestCase):
    def test_0(self):

        resultado=fibonacci(0)

        self.assertEqual(0,fibonacci(0))

    def test_1(self):

        resultado=fibonacci(1)

        self.assertEqual(1,fibonacci(1))

    def test_2 (self):

        resultado=fibonacci(2)

        self.assertEqual(1,fibonacci(2))

    def test_3 (self):

        resultado=fibonacci(3)

        self.assertEqual(2,fibonacci(3))

    def test_4 (self):

        resultado=fibonacci(4)

        self.assertEqual(3,fibonacci(4))

    def test_15(self):
    
        resultadp=fibonacci(15)

        self.assertEqual(610,fibonacci(15))
if __name__ == '__main__':
    unittest.main()