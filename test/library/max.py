
import unittest
class TDDmax(unittest.TestCase):
    def test_max(self):
        # Return the largest item in an iterable or the largest of two or more arguments.
        i=map(lambda x:x**2,[1,2,3])
        self.assertEqual(max(i),9)
        self.assertEqual(max(2,9),9)
        self.assertEqual(max([1,2,9]),9)

if __name__ == '__main__':
    unittest.main()

                