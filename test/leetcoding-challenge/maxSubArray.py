from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot = nums[0]
        # minVal=min(nums)
        for i in range(len(nums)):
            for n in range(i+1,len(nums)+1):
                temp = sum(nums[i :n])
                if tot < temp:
                    tot = temp
        return tot