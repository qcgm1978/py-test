class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret=''
        for i in range(len(s) - 1):
            currentStr=''
            for n in range(i,len(s)):
                sNext = s[n]
                if  sNext in currentStr:
                    break
                else:
                    currentStr = s[i: n + 1]
            if len(currentStr) > len(ret):
                ret = currentStr
        return len(ret) if len(s) > 1 else len(s)