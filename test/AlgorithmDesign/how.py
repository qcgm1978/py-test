# step 1 − START
# step 2 − declare three integers a, b & c
# step 3 − define values of a & b
# step 4 − add values of a & b
# step 5 − store output of step 4 to c
# step 6 − print c
# step 7 − STOP
from typing import List
import sys
class Solution:#1
    def addTwo(self, num1: float, num2: float) -> float:#2,3
        return num1 + num2  #4,5,6,7
        # In binary search we take a sorted list of elements and start looking for an element at the middle of the list. If the search value matches with the middle value in the list we complete the search. Otherwise we eleminate half of the list of elements by choosing whether to procees with the right or left half of the list depending on the value of the item searched. This is possible as the list is sorted and it is much quicker than linear search. Here we divide the given list and conquer by choosing the proper half of the list. We repeat this approcah till we find the element or conclude about it's absence in the list.
    idx0 = 0
    
       
    def bsearch(self,list, idx0, idxn, val):

            if (idxn < idx0):
                return None
            else:
                midval = idx0 + ((idxn - idx0) // 2)
        # Compare the search item with middle most value

                if list[midval] > val:
                    return self.bsearch(list, idx0, midval-1,val)
                elif list[midval] < val:
                    return self.bsearch(list, midval+1, idxn, val)
                else:
                    return midval

    #Solution 4 binary search: while loop
    #     try:
    #         list_size = len(l) - 1
    #     except OverflowError:# when the array is big enough and the algorithm is implemented in a language with fixed-precision arithmetic.
    #         list_size=(l.stop - l.start + l.step - 1) # c.step

    #     idxn = list_size
    #     # Find the middle most value
    #     list=l
    #     while self.idx0 <= idxn:
    #         midval = (self.idx0 + idxn)// 2

    #         if list[midval] == val:
    #             return midval
    # # Compare the value the middle most value
    #         if val > list[midval]:
    #             self.idx0 = midval + 1
    #         else:
    #             idxn = midval - 1

    #     if self.idx0 > idxn:
    #         return None
    minV=-sys.maxsize - 1
    maxV= sys.maxsize