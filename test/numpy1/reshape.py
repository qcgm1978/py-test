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

    def testReshape(self):
        a = np.zeros((10, 2))
        self.assertEqual(type(a), np.ndarray)
        b = a.T
        self.assertEqual((b - a.reshape(2, 10)).any(), 0)
        c = b.view()

        def func(c):
            c.shape = 20

        self.assertRaises(AttributeError, func, c)

    def testOrder(self):
        a = np.arange(6).reshape((3, 2))
        self.assertEqual((a - [[0, 1], [2, 3], [4, 5]]).any(), 0)
        alist = [[0, 1, 2], [3, 4, 5]]
        self.assertEqual(
            np.reshape(a, (2, 3)).tolist(), alist
        )  # C-like index ordering
        a = np.reshape(np.ravel(a), (2, 3))  # equivalent to C ravel then C reshape
        self.assertEqual(a.tolist(),alist)


if __name__ == "__main__":
    unittest.main()

