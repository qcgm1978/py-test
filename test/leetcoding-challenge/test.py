
import unittest
from singleNumber import Solution as Solution1
from isHappy import Solution as Solution2
from maxSubArray import Solution as Solution3
from longestPalindrome import Solution as Solution4
from convert import Solution as Solution5
class TDD_TEST(unittest.TestCase):
    def test_test(self):
        ins=Solution1()
        n=ins.singleNumber([2,2,1])
        n1=ins.singleNumber([4,1,2,1,2])
        self.assertEqual(n,1)
        self.assertEqual(n1, 4)
    def test_isHappy(self):
        ins = Solution2()
        n=ins.isHappy(19)
        n1=ins.isHappy(2)
        n2=ins.isHappy(78)
        n3=ins.isHappy(3)
        n4=ins.isHappy(6)
        n5=ins.isHappy(7)
        self.assertTrue(n)
        self.assertFalse(n1)
        self.assertFalse(n2)
        self.assertFalse(n3)
        self.assertFalse(n4)
        self.assertTrue(n5)
    def test_maxSubArray(self):
        ins = Solution3()
        n=ins.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        n1=ins.maxSubArray([1])
        n2=ins.maxSubArray([-2,1])
        n3=ins.maxSubArray([-1])
        self.assertEqual(n,6)
        self.assertEqual(n1,1)
        self.assertEqual(n2,1)
        self.assertEqual(n3,-1)
    def test_longestPalindrome(self):
        ins = Solution4()
        s=ins.longestPalindrome('babad')
        s1=ins.longestPalindrome('cbbd')
        s2=ins.longestPalindrome('a')
        s3=ins.longestPalindrome('ac')
        s4=ins.longestPalindrome('')
        s5=ins.longestPalindrome("abcba")
        self.assertEqual(s,'bab')
        self.assertEqual(s1,'bb')
        self.assertEqual(s2,'a')
        self.assertEqual(s3,'a')
        self.assertEqual(s4,'')
        self.assertEqual(s5, "abcba")
    def test_convert(self):
        ins = Solution5()
        s=ins.convert(s = "PAYPALISHIRING", numRows = 3)
        s1=ins.convert(s = "PAYPALISHIRING", numRows = 4)
        s2=ins.convert(s = "AB", numRows = 1)
        s3=ins.convert(s = "ABC", numRows = 1)
        self.assertEqual(s,"PAHNAPLSIIGYIR")
        self.assertEqual(s1,"PINALSIGYAHRPI")
        self.assertEqual(s2,"AB")
        self.assertEqual(s3,"ABC")
if __name__ == '__main__':
    unittest.main()

                