# Dot product of two arrays. Specifically,
import unittest
from dotTwo import dotTwo 
import numpy as np
class NumpyTest(unittest.TestCase):
    def setUp(self):
        def assertEqualAll(arr):
            return all(v==arr[0] for v in arr)
        self.assertEqualAll=assertEqualAll
    def test_dot(self):
        dot=np.dot(3, 4)
        bool=self.assertEqualAll([dot,3*4,dotTwo(3,4),12])
        self.assertTrue(bool)
        dot=np.dot([2j, 3j], [2j, 3j])
        dot1=dotTwo([2j, 3j], [2j, 3j])
        bool=self.assertEqualAll([dot,dot1])
        self.assertTrue([dot,dot1,-13,-13+0j])

if __name__ == '__main__':
    unittest.main()        