from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = dict.fromkeys(nums)
        nums=list(k)
        return len(k)
