
import unittest
import collections
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
class TDDzip(unittest.TestCase):
    def test_zip_ret_tuple(self):
         t=zip(['a', 'b', 'c'], (1, 2, 3))
         self.assertEqual(tuple(t),(('a',1),('b',2),('c',3)))
         t1 = zip(['a', 'b'], (1, 2, 3))
         t2 = zip(['a', 'b','c'], (1, 2))
         self.assertEqual(list(t1),[('a',1),('b',2)])
         self.assertEqual(list(t2),[('a',1),('b',2)])
    def test_zip(self):
        # Make an iterator that aggregates elements from each of the iterables.
        x = [1, 2, 3]
        y = [4, 5, 6]
        zipped = zip(x, y)
        self.assertIsInstance(zipped,collections.Iterable)
        self.assertEqual(list(zipped),[(1, 4), (2, 5), (3, 6)])
        x2, y2 = zip(*zip(x, y))
        self.assertIsInstance(x2,collections.Iterable)
        self.assertEqual(x, list(x2))
        self.assertEqual(y, list(y2))
    def test_emulate_zip(self):
        # Make an iterator that aggregates elements from each of the iterables.
        from functional.zip import zip
        x = [1, 2, 3]
        y = [4, 5, 6]
        zipped = zip(x, y)
        self.assertIsInstance(zipped,collections.Iterable)
        self.assertEqual(list(zipped),[(1, 4), (2, 5), (3, 6)])
        x2, y2 = zip(*zip(x, y))
        self.assertIsInstance(x2,collections.Iterable)
        self.assertEqual(x, list(x2))
        self.assertEqual( y, list(y2))

if __name__ == '__main__':
    unittest.main()

                