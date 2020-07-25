import unittest
from builtInAny import getAny
class TestAny(unittest.TestCase):
    def testIterables(self):
        actual = [
            -0.2896346,
            -0.4064693,
            0.66847844,
            0.54833631,
        ]
        self.assertTrue(any(x < 1 for x in actual))
        self.assertTrue(getAny(x < 1 for x in actual))
    def test_any_all(self):
        # The any(iter) and all(iter) built-ins look at the truth values of an iterable’s contents. any() returns True if
# any element in the iterable is a true value, and all() returns True if all of the elements are true values:
        self.assertTrue(any([0, 1, 0]) )
        self.assertFalse(any([0, 0, 0]) )
        self.assertTrue(any([1, 1, 1]) )
        self.assertFalse(all([0, 1, 0]) )
        self.assertFalse(all([0, 0, 0]) )
        self.assertTrue(all([1, 1, 1]))
if __name__ == "__main__":
    unittest.main()
