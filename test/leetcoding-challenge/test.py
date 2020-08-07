
import unittest
from singleNumber import Solution as Solution1
from isHappy import Solution as Solution2
from maxSubArray import Solution as Solution3
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

if __name__ == '__main__':
    unittest.main()

                