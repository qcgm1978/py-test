from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        notNeg = sorted(list(filter(lambda x: x >= 0, nums)), reverse=True)
        neg = sorted(list(filter(lambda x: x < 0, nums)), reverse=True)
        zeros = sorted(list(filter(lambda x: x == 0, nums)), reverse=True)
        ret = [[0, 0, 0]] if len(zeros) >= 3 else []
        for i in range(len(notNeg)):
            if i >= 1 and notNeg[i] == notNeg[i - 1]:
                continue
            for j in range(len(neg) - 1):
                if j >= 1 and neg[j] == neg[j - 1]:
                    continue
                negTol = neg[j] + neg[j + 1]
                sum = notNeg[i] + negTol
                if sum > 0:
                    addend = neg[j + 1] - sum
                    if addend in neg:
                        ret.append(sorted([notNeg[i], neg[j], addend]))
                elif sum == 0:
                    ret.append(sorted([notNeg[i], neg[j], neg[j + 1]]))
                    break
        for i in range(len(neg)):
            if i >= 1 and neg[i] == neg[i - 1]:
                continue
            ele = self.findInList(notNeg, neg[i])
            if ele:
                ret+=ele
        return ret

    def findInList(self, l, addend):
        ret=[]
        for j in range(len(l) - 1):
            if j >= 1 and l[j] == l[j - 1]:
                continue
            notNegTol = l[j] + l[j + 1]
            sum = addend + notNegTol
            if sum > 0 and j + 2 <= len(l) - 1:
                 ele1 = l[j + 1] - sum
                 if ele1 in l:
                    ret.append([l[j],ele1,addend])
            elif sum == 0:
                 ret.append( sorted([addend, l[j], l[j + 1]]))
        return ret

