
import unittest
from singleNumber import Solution as Solution1
from isHappy import Solution as Solution2
from maxSubArray import Solution as Solution3
from longestPalindrome import Solution as Solution4
from convert import Solution as Solution5
from reverse import Solution as Solution6
from myAtoi import Solution as Solution7
from isPalindrome import Solution as Solution8
from isMatch import Solution as Solution9
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
        self.assertEqual(s3, "ABC")
    def test_reverse(self):
        ins=Solution6()
        n=ins.reverse(123)
        n1=ins.reverse(-123)
        n2=ins.reverse(120)
        n3=ins.reverse(1534236469)
        self.assertEqual(n,321)
        self.assertEqual(n1,-321)
        self.assertEqual(n3, 0)
    def test_myAtoi(self):
        ins=Solution7()
        n=ins.myAtoi('42')
        n1=ins.myAtoi("   -42")
        n2=ins.myAtoi("4193 with words")
        n3=ins.myAtoi("words and 987")
        n4=ins.myAtoi("-91283472332")
        n5=ins.myAtoi("  -0012a42")
        n6=ins.myAtoi("2147483648")
        n7=ins.myAtoi("+11e530408314")
        self.assertEqual(n,42)
        self.assertEqual(n1,-42)
        self.assertEqual(n2,4193)
        self.assertEqual(n3,0)
        self.assertEqual(n4,-2147483648)
        self.assertEqual(n5,-12)
        self.assertEqual(n6,2147483647)
        self.assertEqual(n7,11)
    def test_isPalindrome(self):
        ins = Solution8()
        bool=ins.isPalindrome(121)
        bool1=ins.isPalindrome(-121)
        bool2=ins.isPalindrome(10)
        bool3=ins.isPalindrome(11)
        self.assertTrue(bool)
        self.assertFalse(bool1)
        self.assertFalse(bool2)
        self.assertTrue(bool3)
    def test_isMatch(self):
        ins = Solution9()
        bool=ins.isMatch("aa",'a')
        bool1=ins.isMatch("aa",'a*')
        bool2=ins.isMatch("ab",'.*')
        bool3=ins.isMatch("aab",p = "c*a*b")
        bool4=ins.isMatch("mississippi",p = "mis*is*p*.")
        bool5=ins.isMatch("ab",".*c")
        self.assertFalse(bool)
        self.assertTrue(bool1)
        self.assertTrue(bool2)
        self.assertTrue(bool3)
        self.assertFalse(bool4)
        self.assertFalse(bool5)
if __name__ == '__main__':
    unittest.main()

                