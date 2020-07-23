
import unittest
class TDDsum(unittest.TestCase):
    def test_sum(self):
    #    Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.
        self.assertEqual(sum(map(lambda x:x**2,[1,2])),5)

if __name__ == '__main__':
    unittest.main()

                