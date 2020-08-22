import unittest
from generateParenthesis import Solution
from mergeKLists import ListNode,Solution as Solution2
from swapPairs import ListNode as ListNode1,Solution as Solution3
from removeDuplicates import Solution as Solution4
from removeElement import Solution as Solution5
from divide import Solution as Solution6

class TDD_TEST11(unittest.TestCase):
    def test_generateParenthesis(self):
        ins = Solution()
        n = ins.generateParenthesis(3)
        n1 = ins.generateParenthesis(1)
        self.assertCountEqual(n, [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ])
        self.assertCountEqual(n1,['()'])
    def test_mergeKLists(self):
        ins = Solution2()
        l=ins.mergeKLists([ListNode([1,4,5]),ListNode([1,3,4]),ListNode([2,6])])
        self.assertEqual(l,[1,1,2,3,4,4,5,6])
    def test_swapPairs(self):
        ins = Solution3()
        l=ins.swapPairs(ListNode1([1,2,3,4]))
        self.assertEqual(l.val,ListNode1([2,1,4,3]).val)
    def test_removeDuplicates(self):
        ins = Solution4()
        n=ins.removeDuplicates([1,1,2])
        n1=ins.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        self.assertEqual(n,2)
        self.assertEqual(n1,5)
    def test_removeElement(self):
        ins = Solution5()
        n=ins.removeElement(nums = [3,2,2,3], val = 3)
        n1=ins.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
        self.assertEqual(n,2)
        self.assertEqual(n1,5)
    def test_divide(self):
        ins = Solution6()
        n=ins.divide(10,3)
        n1=ins.divide(dividend = 7, divisor = -3)
        n2=ins.divide(dividend = -1, divisor = 1)
        n3=ins.divide(-2147483648,-1)
        n4=ins.divide(2147483647,3)
        self.assertEqual(n,3)
        self.assertEqual(n1,-2)
        self.assertEqual(n2,-1)
        self.assertEqual(n3,2**31-1)
        self.assertEqual(n4,715827882)
if __name__ == '__main__':
    unittest.main()

                