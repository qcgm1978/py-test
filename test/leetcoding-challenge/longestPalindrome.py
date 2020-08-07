class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for i in range(len(s) - 1):
            for n in range(i + 1, len(s)):
                minus = n - i
                middle = minus // 2
                if (minus) % 2:
                    left = s[i : middle+1+i ]
                else:
                    left = s[i : middle+i ]
                right = "".join(list(reversed(s[middle+1+i:n+1])))
                if left == right:
                    temp = s[i : n+1 ]
                    if len(temp) > len(ret):
                        ret = temp
        return ret if len(ret) > 1 else (s[0] if len(s) else "")

