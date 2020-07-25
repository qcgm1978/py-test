import unittest
import itertools,collections
class test_count(unittest.TestCase):
    def test_count(self):
        i=itertools.count(10)
        self.assertIsInstance(i,collections.Iterable)
        self.assertIsInstance([i],collections.Iterable)
        self.assertIsInstance([i],list)
    def test_repeat(self):
        r=itertools.repeat('abc',5)
        self.assertIsInstance(r, collections.Iterable)
        self.assertEqual(list(r),['abc','abc','abc','abc','abc'])
    def test_chain(self):
         c=itertools.chain(['a', 'b', 'c'], (1, 2, 3))
         self.assertEqual(tuple(c), ('a', 'b', 'c', 1, 2, 3))
    def test_slice(self):
        i=itertools.islice(range(10), 3)
        self.assertEqual(list(i), [0, 1, 2])
        i1=itertools.islice(range(10), 2, 8)
        self.assertEqual(list(i1),[2,3,4,5,6,7])
        i2 = itertools.islice(range(10), 2, 8, 2)
        self.assertEqual(list(i2),[2,4,6])
    def test_tee(self):
        t=itertools.tee(itertools.count())
        self.assertTrue(isinstance(t, collections.Iterable))
        # where iterA
if __name__ == '__main__':
    unittest.main()