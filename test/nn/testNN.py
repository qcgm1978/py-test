import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from nn import nn  # pylint: disable=import-error
import numpy as np

import others.mock
from testfixtures import compare, RoundComparison as R


class TDDNN(unittest.TestCase):
    def test_nn(self):
        a = nn()
        val = a["l1"]
        b = nn(1)
        val1 = b["l1"]
        self.assertEqual(type(val), np.ndarray)
        self.assertEqualAll(len(val), len(val1), 4)
        # print(val.tolist())
        # print(val1.tolist())
        alist = (val - val1).tolist()
        # print(alist)
        fact = [R(v[0], 8) for v in alist]
        actual = [
            -0.2896346,
            -0.4064693,
            0.66847844,
            0.54833631,
        ]
        compare(True, True)
        compare(fact, actual)
        self.assertTrue(all(x < 1 for x in val))
        e=a['l1_error']
        e1=b['l1_error']
        print(e)
        # print(e1)

if __name__ == "__main__":
    unittest.main()
