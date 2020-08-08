from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height) - 1):
            for j in range(i+1,len(height)):
                temp = (j - i) * min(height[i], height[j])
                area = temp if temp>area else area
        return area