class Solution:
    def reverse(self, x: int) -> int:
        rev= int(''.join(list(reversed(str(abs(x))))))
        ret= rev if x>=0 else -rev
        return ret if -2**31-1<=ret<=2**31-1 else 0