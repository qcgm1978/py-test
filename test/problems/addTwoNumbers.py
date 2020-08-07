# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = second = 0
        l1=l1.val
        l2=l2.val
        for i in range(len(l1)):
            first += l1[i] * (10 ** i)
        for i in range(len(l2)):
            second += l2[i] * (10 ** i)
        tot = first + second
        l = []
        ret= list(map(int,list(reversed(str(tot)))))
        return ListNode(ret)