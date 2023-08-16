#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 1
#   To use this, run: python test_a1.py
#   Tested using Python 3.10
#

import unittest
from a1 import factorial, fibonacci, sum


class A1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    


    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)
        self.assertEqual(fibonacci(35),9227465)

    def test_sum(self):
        self.assertEqual(sum(0),0)
        self.assertEqual(sum(1),1)
        self.assertEqual(fibonacci(2),3)
        self.assertEqual(fibonacci(376),70876)
        self.assertEqual(fibonacci(35),630)


 
if __name__ == '__main__':
    unittest.main()