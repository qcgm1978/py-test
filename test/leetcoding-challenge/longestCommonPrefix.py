from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret=''
        if not len(strs):
            return ret
        minLen = sorted(list(map(len, strs)))[0]
        for i in range(minLen):
            l = list(map(lambda x: x[i] == strs[0][i], strs))
            if all(l):
                ret += strs[0][i]
            else:
                return ret 
        return ret 
        