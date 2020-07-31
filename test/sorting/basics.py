import unittest


class TDD_BASICS(unittest.TestCase):
    def test_basics(self):
        l = [5, 2, 3, 1, 4]
        s = sorted(l)
        asc = [1, 2, 3, 4, 5]
        self.assertEqual(s, asc)
        l.sort()
        self.assertEqual(l,asc)
        d = {2: 'B',1: 'D',  3: 'B', 4: 'E', 5: 'A'}
        l1=sorted(d)
        self.assertEqual(l1, asc)
        self.assertRaises(AttributeError,lambda:d.sort())

if __name__ == "__main__":
    unittest.main()

