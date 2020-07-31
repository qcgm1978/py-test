# Return e raised to the power x, minus 1. Here e is the base of natural logarithms. For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision; the expm1() function provides a way to compute this quantity to full precision:
import unittest
from math import exp,expm1
class TDD_EXPM1(unittest.TestCase):
    def test_expm1(self):
        e=exp(1e-5) - 1  # gives result accurate to 11 places
        self.assertEqual(e,1.0000050000069649e-05)
        e1=expm1(1e-5)# result accurate to full precision
        self.assertEqual(e1,1.0000050000166668e-05)

if __name__ == '__main__':
    unittest.main()

                