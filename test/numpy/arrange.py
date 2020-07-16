import unittest
import numpy as np
from getByArrange import getByArrange
class NumpyTest(unittest.TestCase):
    def testArrange(self):
        a=np.arange(3)
        self.assertFalse((a-[0,1,2]).any())
        self.assertFalse((a-getByArrange(3)).any())
        self.assertFalse((np.arange(3.0)-[0.,1.,2.]).any())
        self.assertFalse((np.arange(3.0)-getByArrange(3.0)).any())
        self.assertFalse((np.arange(3,7)-[3,4,5,6]).any())
        self.assertFalse((np.arange(3,7)-getByArrange(3,7)).any())
        self.assertFalse((np.arange(3,7,2)-[3,5]).any())
        self.assertFalse((np.arange(3,7,2)-getByArrange(3,7,2)).any())
if __name__ == "__main__":
    unittest.main()