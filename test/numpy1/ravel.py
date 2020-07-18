# Dot product of two arrays. Specifically,
import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append("/Users/zhanghongliang/Documents/py-test")

import numpy as np  # pylint: disable=import-error

print(sys.version)


class NumpyTest(unittest.TestCase):
    def setUp(self):
        def assertEqualAll(arr):
            return all(v == arr[0] for v in arr)

        self.assertEqualAll = assertEqualAll

    def testFlatten(self):
        x = np.array([[1, 2, 3], [4, 5, 6]])
        a=np.ravel(x).tolist()
        self.assertEqual(a,[1,2,3,4,5,6])
if __name__ == "__main__":
    unittest.main()

