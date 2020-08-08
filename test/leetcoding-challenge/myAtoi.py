import re
class Solution:
    def myAtoi(self, str: str) -> int:
        try:
            num = int(str)
        except ValueError:
            matchNum=re.match(r'\s*([-+]?\d+)', str)
            num=int(matchNum.group()) if matchNum else 0
        ret=num if -2**31<num<2**31 else (-2**31 if num <0 else 2**31-1)
        return ret
