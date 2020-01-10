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
    
   

    def test_num(self):
        self.assertTrue(is_it_true(1))
        self.assertFalse(is_it_true(0.0))
        self.assertTrue(is_it_true(fractions.Fraction(1, 2)))
        self.assertFalse(is_it_true(fractions.Fraction(0, 2)))

if __name__ == '__main__':
    unittest.main()
