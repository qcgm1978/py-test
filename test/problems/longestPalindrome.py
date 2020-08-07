class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for i in range(len(str) - 1):
            ret=s[i]
            for n in range(len(str)):
                temp=ret+s[n]
        return s