import unittest
class TestIs(unittest.TestCase):
    def testSameObj(self):
        x = ["apple", "banana", "cherry"]
        y = x
        self.assertTrue(x is y)
        self.assertTrue(y is x)
        self.assertIs(x,y)
    def eqlObj(self):
        x = ["apple", "banana", "cherry"]
        y = ["apple", "banana", "cherry"]
        self.assertIs(x,y)
if __name__ == "__main__":
    unittest.main()
