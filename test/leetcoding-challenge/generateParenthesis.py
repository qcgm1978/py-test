from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret=["()"]
        m=n
        while True:
            if m == 1:
                return list(dict.fromkeys(ret))
            l = ret
            ret=[]
            length = len(l)
            for j in range(length):
                string = l[j]
                for k in range(len(string)):
                    ret.append(string[:k] + "()" + string[k:])
            m-=1
