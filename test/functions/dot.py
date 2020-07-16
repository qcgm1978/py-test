# Dot product of two arrays. Specifically,
import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append("/Users/zhanghongliang/Documents/py-test")

from dotTwo import dotTwo
import numpy as np  # pylint: disable=import-error

print(sys.version)


class NumpyTest(unittest.TestCase):
    def setUp(self):
        def assertEqualAll(arr):
            return all(v == arr[0] for v in arr)

        self.assertEqualAll = assertEqualAll

    def test_dot(self):
        dot = np.dot(3, 4)
        bool = self.assertEqualAll([dot, 3 * 4, dotTwo(3, 4), 12])
        self.assertTrue(bool)
        dot = np.dot([2j, 3j], [2j, 3j])
        dot1 = dotTwo([2j, 3j], [2j, 3j])
        bool = self.assertEqualAll([dot, dot1])
        self.assertTrue([dot, dot1, -13, -13 + 0j])
        a = [[1, 0], [0, 1]]
        b = [[4, 1], [2, 2]]
        c = dotTwo(a, b)
        d = np.dot(a, b)
        self.assertEqualAll([(c - d).any(), 0])
        a = np.arange(3 * 4 * 5 * 6).reshape((3, 4, 5, 6))
        # print(a)
        b = np.arange(3 * 4 * 5 * 6)[::-1].reshape((5, 4, 6, 3))
        ab=np.dot(a, b)
        print(len(ab))
        # ab1=dotTwo(a,b)

        ab[2, 3, 2, 1, 2, 2]


if __name__ == "__main__":
    unittest.main()

