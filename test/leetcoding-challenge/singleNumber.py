from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[:i] + nums[i + 1 :]:
                continue
            else:
                return nums[i]