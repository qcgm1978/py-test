from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        tot = 0
        minus=10**6
        length=len(nums)
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                twoSum=nums[i]+ nums[j]
                for k in range(j+1,length):
                    temp = twoSum+ nums[k]
                    if abs(temp - target) < minus:
                        minus = abs(temp - target)
                        tot=temp
        return tot