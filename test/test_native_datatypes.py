import unittest
import fractions
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

   


if __name__ == '__main__':
    unittest.main()
