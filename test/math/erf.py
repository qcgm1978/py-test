# Return the error function at x.
import unittest
from math import erf,sqrt
class TDD_ERF(unittest.TestCase):
    def test_erf(self):
        def phi(x):
            'Cumulative distribution function for the standard normal distribution'
            return (1.0 + erf(x / sqrt(2.0))) / 2.0
        self.assertEqual(phi(1),0.8413447460685429)

if __name__ == '__main__':
    unittest.main()

                