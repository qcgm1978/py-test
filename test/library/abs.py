import unittest
import math


class TDDabs(unittest.TestCase):
    def test_abs(self):
        # Return the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned. If x defines __abs__(), abs(x) returns x.__abs__().
        self.assertEqual(abs(-1), 1)
        self.assertIsInstance(-1, int)
        self.assertEqual(abs(-1.1), 1.1)
        self.assertIsInstance(-1.1, float)
        c = complex(-math.sqrt(2), -math.sqrt(7))
        self.assertAlmostEqual(abs(c), 3)
        self.assertIsInstance(c, complex)
        class employee:
            def __new__(cls):
                # print ("__new__ magic method is called")
                inst = object.__new__(cls)
                return inst
            def __init__(self):
                # print ("__init__ magic method is called")
                self.name = 'Satya'
            def __abs__(self):
                return 2
        e1 = employee()
        self.assertEqual(e1.name,'Satya')
        self.assertEqual(abs(e1), 2)
        self.assertEqual(e1.__abs__(), 2)
        self.assertTrue(callable(e1.__abs__))


if __name__ == "__main__":
    unittest.main()

