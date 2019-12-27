import os,glob
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error


class TDDDiveIntoPython3(unittest.TestCase):

    def test_set(self):
        a_set=set(range(10))
        self.assertEqual(a_set,{0,1,2,3,4,5,6,7,8,9})
        square={x ** 2 for x in a_set}
        self.assertEqual(square,{0,1,4,9,16,25,36,49,64,81})
        even={x for x in a_set if x % 2==0}
        self.assertEqual(even,{0,2,4,6,8})
        two_pows={2**x for x in range(10)}
        self.assertEqual(two_pows,{1,2,4,8,16,32,64,128,256,512})

    

if __name__ == '__main__':
    unittest.main()
