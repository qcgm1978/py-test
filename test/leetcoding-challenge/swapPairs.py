# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        val = head.val
        ret=[]
        for i in range(len(val)):
            if i % 2:
                ret.append(temp)
            else:
                temp=val[i]
                ret.append(val[i+1])
        return ListNode(ret)