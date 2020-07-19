import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error
from app.nn import nn  # pylint: disable=import-error
import numpy as np
import logging

import others.mock
from testfixtures import compare, RoundComparison as R
from decimal import Decimal


class TDDDiveIntoPython3(unittest.TestCase):
    def test_current(self):
        size = approximate_size(4000, a_kilobyte_is_1024_bytes=False)
        self.assertEqual(size, "4.0 KB")

    def test_nn(self):
        val = nn()
        val1 = nn(1)
        self.assertEqual(type(val), np.ndarray)
        self.assertEqualAll(len(val), len(val1), 4)
        # print(val.tolist())
        # print(val1.tolist())
        alist = (val - val1).tolist()
        # print(alist)
        actual = [
            -0.2896346,
            -0.4064693,
            0.66847844,
            0.54833631,
        ]
        fact = [R(v[0], 8) for v in alist]
        compare(fact, actual)


if __name__ == "__main__":
    unittest.main()
