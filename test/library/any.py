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
        pass
if __name__ == "__main__":
    unittest.main()
