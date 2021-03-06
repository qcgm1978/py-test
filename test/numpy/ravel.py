# Dot product of two arrays. Specifically,
import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append("/Users/zhanghongliang/Documents/py-test")

import numpy as np  # pylint: disable=import-error
from getRavel import getRavel
import others.mock
class NumpyTest(unittest.TestCase):
    def testFlatten(self):
        x = np.array([[1, 2, 3], [4, 5, 6]])
        a=np.ravel(x).tolist()
        self.assertEqualAll(a, x.reshape(-1).tolist(),x.reshape(1,6).tolist()[0], [1, 2, 3, 4, 5, 6])
        b = np.ravel(x, order='F').tolist()
        self.assertEqualAll(b,[1,4,2,5,3,6],getRavel(x,order='F'))
if __name__ == "__main__":
    unittest.main()

