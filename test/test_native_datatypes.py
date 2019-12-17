import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    def test_test(self):
        self.assertEqual(4, True*4)
    def test_num_operate(self):
        self.assertEqual(11 / 2, 5.5)
        self.assertEqual(11//2,5)
        self.assertEqual(-11//2,-6)
        self.assertEqual(11.0//2,5.0)
        self.assertEqual(11.0**2,121.0)
        self.assertEqual(11.0 % 2, 1.0)
    def test_fractions(self):
        self.assertTrue(fractions)
        self.assertTrue(callable(fractions.Fraction))
        self.assertFalse(callable(fractions.Fraction(1,3)))
        self.assertFalse(callable(fractions.Fraction(1, 3) * 2))
        self.assertRaises(ZeroDivisionError, fractions.Fraction, 1, 0)

    def test_Trigonometry(self):
        self.assertTrue(math)
        self.assertAlmostEqual(math.pi,3.14,2)
        self.assertEqual(math.sin(math.pi/2),1.0)
        self.assertAlmostEqual(round(math.tan(math.pi/4),2),1.0,2)
   


if __name__ == '__main__':
    unittest.main()
