import unittest
import fractions

def is_it_true(anything):
        if anything:
            return True
        else:
            return False
class TddInPython(unittest.TestCase):

    def test_test(self):
        self.assertEqual(4, True*4)
    
   

    def test_num(self):
        self.assertTrue(is_it_true(1))
        self.assertFalse(is_it_true(0.0))
        self.assertTrue(is_it_true(fractions.Fraction(1, 2)))
        self.assertFalse(is_it_true(fractions.Fraction(0, 2)))

if __name__ == '__main__':
    unittest.main()
