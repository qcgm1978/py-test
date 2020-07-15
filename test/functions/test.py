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


class TDDDiveIntoPython3(unittest.TestCase):

    def test_current(self):
        size=approximate_size(4000, a_kilobyte_is_1024_bytes=False)
        self.assertEqual( size,'4.0 KB')
    def test_nn(self):
        val=nn()
        val1=nn(1)
        self.assertEqual(type(val),np.ndarray)
        self.assertEqual(len(val),4)
        actual=[[ 0.29929909],
       [ 0.41433436],
       [ 0.32511054],
       [ 0.44378327]]
        print val1
        print actual
        self.assertEqual((val1-actual).all(),1)
        self.assertLess((val1-actual)[0],1e-8)
    
if __name__ == '__main__':
    unittest.main()
