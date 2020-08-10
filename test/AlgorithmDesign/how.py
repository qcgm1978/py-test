# step 1 − START
# step 2 − declare three integers a, b & c
# step 3 − define values of a & b
# step 4 − add values of a & b
# step 5 − store output of step 4 to c
# step 6 − print c
# step 7 − STOP
from typing import List
class Solution:#1
    def addTwo(self, num1: float, num2: float) -> float:#2,3
        return num1 + num2  #4,5,6,7
        # In binary search we take a sorted list of elements and start looking for an element at the middle of the list. If the search value matches with the middle value in the list we complete the search. Otherwise we eleminate half of the list of elements by choosing whether to procees with the right or left half of the list depending on the value of the item searched. This is possible as the list is sorted and it is much quicker than linear search. Here we divide the given list and conquer by choosing the proper half of the list. We repeat this approcah till we find the element or conclude about it's absence in the list.
    idx0 = 0
    
    def bsearch(self, l: List[float], val: float) -> int:
        # linear search
        # Solution 1
        # for i in range(len(l)):
        #     if l[i] == val:
        #         return i
        # return None
        # Solution 2
        # try:
        #     return l.index(val)
        # except ValueError:
        #     return None
        # Solution 3: binary search: recursion
        
        # middle = len(l) // 2
        # if l[middle] == val:
        #     return self.idx0+middle
        # elif middle==0 or middle==len(l):
        #     return None
        # else:
        #     if l[middle]>val:
        #         l1 = l[0:middle]
        #     else:
        #         l1 = l[middle:]
        #         self.idx0+=middle
        #     return self.bsearch(l1, val)
    #Solution 4 binary search: while loop
        list_size = len(l) - 1
        idxn = list_size
        # Find the middle most value
        list=l
        while self.idx0 <= idxn:
            midval = (self.idx0 + idxn)// 2

            if list[midval] == val:
                return midval
    # Compare the value the middle most value
            if val > list[midval]:
                self.idx0 = midval + 1
            else:
                idxn = midval - 1

        if self.idx0 > idxn:
            return None