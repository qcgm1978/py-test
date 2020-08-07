
import unittest
from two_sum import Solution
from addTwoNumbers import Solution2,ListNode
from lengthOfLongestSubstring import Solution3
from findMedianSortedArrays import Solution as Solution4
from longestPalindrome import Solution as Solution5
class TDD_TEST(unittest.TestCase):
    def test_test(self):
        nums = [2, 7, 11, 15]
        target = 9
        ins=Solution()
        l = ins.twoSum(nums, target)
        self.assertEqual(l, [0, 1])
    def test_add_two_numbers(self):
        ins = Solution2()
        node1 = ListNode([2, 4, 3])
        print(node1.next)
        l = ins.addTwoNumbers(node1,ListNode( [5, 6, 4]))
        self.assertEqual(l.val, ListNode([7, 0, 8]).val)
    def test_lengthOfLongestSubstring(self):
        ins = Solution3()
        long = ins.lengthOfLongestSubstring('abcabcbb')
        long1 = ins.lengthOfLongestSubstring('bbbbb')
        long2 = ins.lengthOfLongestSubstring('pwwkew')
        long3 = ins.lengthOfLongestSubstring(" ")
        long4 = ins.lengthOfLongestSubstring("")
        self.assertEqual(long,3)
        self.assertEqual(long1,1)
        self.assertEqual(long2,3)
        self.assertEqual(long3,1)
        self.assertEqual(long4, 0)
    def test_findMedianSortedArrays(self):
        ins = Solution4()
        nums1 = [1, 3]
        nums2 = [2]
        val = ins.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(val, 2.0)
        nums1 = [1, 2]
        nums2 = [3, 4]
        val = ins.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(val, 2.5)
        nums1=[3]
        nums2=[-2,-1]
        val = ins.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(val, -1)
    def test_longestPalindrome(self):
        ins = Solution5()
        s = ins.longestPalindrome('babad')
        self.assertEqual(s,'bab')
if __name__ == '__main__':
    unittest.main()

                