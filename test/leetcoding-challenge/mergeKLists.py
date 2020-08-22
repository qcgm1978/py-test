# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.first = lists[0].val
        length=len(self.first)
        middle = length // 2
        for j in range(1,len(lists)):
            start=0
            for i in range(len(lists[j].val)):
                start=self.recursion(start,end=len(self.first),ele=lists[j].val[i])
        return self.first
    def recursion(self, start, end,ele):
        middle = start+(end - start) // 2
        valMiddle=self.first[middle]
        if ele == valMiddle:
            self.first = self.first[:middle] + [ele] + self.first[middle:]
            return middle
        elif ele > valMiddle:
            if middle+1 == end:
                self.first = self.first[: middle + 1] + [ele] + self.first[middle + 1 :]
                return middle
            else:
                return self.recursion(start=middle,end=end,ele=ele)
        else:
            if middle == start:
                self.first = self.first[: middle - 1] + [ele] + self.first[middle - 1 :]
                return middle
            else:
                return self.recursion(start=start,end=middle,ele=ele)