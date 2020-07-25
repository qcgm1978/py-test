import unittest
import os, itertools, collections


class test_count(unittest.TestCase):
    def test_starmap(self):
        i = itertools.starmap(
            os.path.join,
            [
                ("/bin", "python"),
                ("/usr", "bin", "java"),
                ("/usr", "bin", "perl"),
                ("/usr", "bin", "ruby"),
            ],
        )
        self.assertIsInstance(i, collections.Iterable)
        self.assertEqual(list(i), ['/bin/python', '/usr/bin/java', '/usr/bin/perl', '/usr/bin/ruby'])
    def test_select(self):
        def is_even(num):return not num%2
        itertools.filterfalse(is_even, itertools.count())
        def less_than_10(x): return x < 10
        i = itertools.takewhile(less_than_10, itertools.count())
        self.assertEqual(list(i), list(range(0, 10)))
        i1 = itertools.starmap(less_than_10, itertools.count())
        self.assertRaises(TypeError,lambda:list(i1))
        i2=itertools.takewhile(is_even, itertools.count())
        self.assertEqual(tuple(i2),(0,))
        i3 = itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True])
        self.assertIsInstance(i3, collections.Iterable)
        self.assertEqual(list(i3),[1,2,5])

if __name__ == "__main__":
    unittest.main()
