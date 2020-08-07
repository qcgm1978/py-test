from operator import itemgetter
import unittest,collections
class TDDsorted(unittest.TestCase):
    def test_sorted(self):
        nums1=[3]
        nums2 = [-2, -1]
        # nums1 = [1, 2]
        # nums2 = [3, 4]
        res=sorted(nums1+nums2)
        self.assertIsInstance(res,collections.Iterable)
        n=len(res)
        self.assertEqual(res[n//2],-1)
        student_tuples = [
            ('john', 'A', 15),
            ('jane', 'B', 12),
            ('dave', 'B', 10),
        ]
        s = sorted(student_tuples, key=itemgetter(2), reverse=True)
        self.assertIsInstance(s,collections.Iterable)
        
if __name__ == '__main__':
    unittest.main()

                