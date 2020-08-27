# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
import unittest
class TDD_OPERATORS(unittest.TestCase):
    def test_Arithmetic_operators(self):
        self.assertEqual(5**2,25)
    def test_Assignment(self):
        x = 1
        x&=0
        self.assertEqual(x,0)
    def test_comparison(self):
        self.assertTrue(1!=2)
    def test_logical(self):
        x = 1
        self.assertFalse(not(x<5 and x<10))
    def test_identity(self):
        a = 1
        b=1
        self.assertTrue(a is b)
        x = {}
        y = x
        self.assertTrue(x is y)
        z = {}
        self.assertTrue(x is not z)
    def test_membership(self):
        self.assertTrue(1 in [1,2])
        self.assertTrue('a' in ('a','b'))
        self.assertTrue('a' not in ('c','b'))
    def test_bitwise(self):
        self.assertFalse(1>>2)
if __name__ == '__main__':
    unittest.main()

                