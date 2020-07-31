# Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:
import unittest,math
class TDD_FSUM(unittest.TestCase):
    def test_fsum(self):
        s=sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
        self.assertEqual(s,0.9999999999999999)
        s1=math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
        self.assertEqual(s1,1.0)

if __name__ == '__main__':
    unittest.main()

                