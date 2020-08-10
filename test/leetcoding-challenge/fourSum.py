from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target=target
        notNeg = sorted(list(filter(lambda x: x > self.target, nums)), reverse=True)
        neg = sorted(list(filter(lambda x: x < self.target, nums)), reverse=True)
        zeros = sorted(list(filter(lambda x: x == self.target, nums)), reverse=True)
        ret = [[self.target, self.target, self.target,self.target]] if len(zeros) >= 4 and ~self.target else []
        for i in range(len(notNeg)):
            if i >= 1 and notNeg[i] == notNeg[i - 1]:
                continue
            for j in range(len(neg) - 2):
                if j >= 1 and neg[j] == neg[j - 1]:
                    continue
                negTol = neg[j] + neg[j + 1]+ neg[j + 2]
                fourSum = notNeg[i] + negTol
                if fourSum > self.target:
                    addend = neg[j + 2] - fourSum
                    if addend in neg:
                        ret.append(sorted([notNeg[i], neg[j],neg[j + 1], addend]))
                elif fourSum == self.target:
                    ret.append(sorted([notNeg[i], neg[j], neg[j + 1], neg[j + 2]]))
                    break
        for i in range(len(neg)):
            if i >= 1 and neg[i] == neg[i - 1]:
                continue
            ele = self.findInList(notNeg, neg[i])
            if i+1<len(neg):
                ele1 = self.findInList(notNeg, neg[i],neg[i+1])
            ret+=ele if ele else []
            ret+=ele1 if ele1 else []
        return ret

    def findInList(self, l, addend,addend1=0):
        ret=[]
        for j in range(len(l) - 2):
            if j >= 1 and l[j] == l[j - 1]:
                continue
            notNegTol = l[j] + l[j + 1]+ l[j + 2]
            sum = addend + notNegTol
            if sum > self.target and j + 3 <= len(l) - 1:
                 ele1 = l[j + 2] - sum
                 if ele1 in l:
                    ret.append(sorted([l[j],l[j + 1],ele1,addend]))
            elif sum == self.target:
                 ret.append( sorted([addend, l[j], l[j + 1],l[j + 2]]))
        return ret

