
import unittest
class TDDreversed(unittest.TestCase):
    def test_reversed(self):
        # reversed(seq)
        # Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
        import collections
        l = [1, 2, 3]
        r=reversed(l)
        self.assertIsInstance(r,collections.Iterable)
        alist=[]
        for i in r:
            alist.append(i)
        self.assertEqual(alist, [3, 2, 1])
        class Seq:
            def __reversed__(self):
                return [1,2]
        s = Seq()
        self.assertIsInstance(s, Seq)
        r = reversed(s)
        self.assertEqual(r,[1,2])
if __name__ == '__main__':
    unittest.main()

                