
import unittest
class TDDiterators(unittest.TestCase):
    def test_iterators(self):
        L = [1, 2, 3]
        it = iter(L)
        self.assertEqual(it.__next__(),1) # same as next(it) 1
        self.assertEqual(next(it) ,2)
        self.assertEqual(next(it) ,3)
        
        self.assertRaises(StopIteration,lambda:next(it))
    def test_iter_as(self):
        # Iterators can be materialized as lists or tuples by using the list() or tuple() constructor functions:
        L = [1, 2, 3]
        iterator = iter(L)
        t = tuple(iterator)
        self.assertIsInstance(t, tuple)
        self.assertEqual(t, (1, 2, 3))
    def test_unpack(self):
        L = [1, 2, 3]
        iterator = iter(L)
        a, b, c = iterator
        self.assertRaises(StopIteration,lambda:next(iterator))
        self.assertEqual(a,1)
        self.assertEqual(b,2)
        self.assertEqual((a,b,c),tuple(iter(L)))
    def test_sequence_iter(self):
        m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        d={}
        for key in m:
             d[key] = m[key]
        self.assertEqual(d, m)
    def test_dict_iter_tuple(self):
        L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
        self.assertEqual(dict(iter(L)),{'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'} )
        self.assertEqual(list(iter(L)),L)
        
if __name__ == '__main__':
    unittest.main()

                