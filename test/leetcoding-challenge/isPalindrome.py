class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            neg=int(''.join(list(reversed(str(x)))))
            return x == neg
        except ValueError:
            return False