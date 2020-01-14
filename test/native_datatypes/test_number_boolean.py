import unittest,os,sys
import fractions
from functools import partial
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error

def is_it_true(anything):
        if anything:
            return True
        else:
            return False
class TddInPython(unittest.TestCase):

    def test_bool(self):
        self.assertRaises(ValueError,partial(approximate_size,-1))
        size=1
        self.assertFalse(size<0)
        size=0
        self.assertFalse(size<0)
        size=-1
        self.assertTrue(size<0)
        self.assertEqual(True+True,2)
        self.assertEqual(True-False,1)
        self.assertEqual(True*False,0)
        self.assertRaises(ZeroDivisionError,lambda: True/False)
    
    def test_numbers(self):
       self.assertIsInstance(1,int)
       self.assertTrue(isinstance(1,int))
       self.assertEqual(1+1.0,2.0)
       self.assertIsInstance(2.0,float)

    def test_num(self):
        self.assertTrue(is_it_true(1))
        self.assertFalse(is_it_true(0.0))
        self.assertTrue(is_it_true(fractions.Fraction(1, 2)))
        self.assertFalse(is_it_true(fractions.Fraction(0, 2)))

if __name__ == '__main__':
    unittest.main()
