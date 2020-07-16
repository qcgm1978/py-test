import unittest
import numpy as np

from isAny import isAny

class NumpyTest(unittest.TestCase):
    def testAny(self):
        a = [1]
        b = [1]
        with self.assertRaises(TypeError) as cm:
            a - b
        the_exception = cm.exception
        error =  "unsupported operand type(s) for -: 'list' and 'list'"
        self.assertEqual(str(the_exception), error)
        self.assertTrue(isAny(a,b))
        bool=np.any([[True, False], [True, True]])
        bool1=isAny([[True, False], [True, True]])
        self.assertEqual(bool,1)
        self.assertEqual(bool1,1)
        arr=np.any([[True, False], [False, False]], axis=0)
        arr1=isAny([[True, False], [False, False]], axis=0)
        self.assertEqual(type(arr),np.ndarray)
        self.assertEqual((arr-[True, False]).any(),0)
        self.assertEqual((arr1-[True, False]).any(),0)
        self.assertTrue(np.any([-1, 0, 5]))
        self.assertTrue(np.any(np.nan))
        o=np.array(False)
        self.assertFalse(o)
        z=np.any([-1, 4, 5], out=o)#Alternate output array in which to place the result.
        self.assertTrue(o)
        self.assertTrue(z)
        self.assertIs(o,z)
        self.assertEqual(type(id(o)),int)
        self.assertEqual(id(z), id(o))
        a = np.arange(3)
        self.assertEqual(type(a),np.ndarray)
        self.assertFalse(np.any([0,0,0]))
        self.assertFalse((a-[0,1,2]).any())
        arr = (a - [0, 1, 2])
        self.assertFalse(arr.any())


if __name__ == "__main__":
    unittest.main()
