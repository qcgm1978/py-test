import unittest, itertools

class TestPermutation(unittest.TestCase):
    def test_combinatorics(self):
        perms=itertools.permutations([1,2,3],2)#	The permutations() function takes a sequence (here a list of three integers) and a number, which is the number of items you want in each smaller group
        perm_next=next(perms)
        self.assertEqual(perm_next,(1,2))
        self.assertEqual(next(perms),(1,3))
        self.assertEqual(next(perms),(2,1))
        self.assertEqual(next(perms),(2,3))
        self.assertEqual(next(perms),(3,1))
        self.assertEqual(next(perms),(3,2))
        self.assertRaises(StopIteration,lambda: next(perms))

    def test_permutation_str(self):
        perms=itertools.permutations('ABC',3)
        self.assertEqual(next(perms),('A','B','C'))
        self.assertEqual(next(perms),('A','C','B'))
        #todo return data types and go on after some time
















if __name__ == "__main__":
    unittest.main()