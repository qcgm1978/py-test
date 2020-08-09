from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = list(digits)
        c = list(map(self.getChr, l))
        length = len(c)
        if length == 1:
            return c[0]
        ret=[]
        for j in range(len(c[0])):
            s =c[0][j]
            for i in range(1, length):
                for k in range(len(c[0])):
                    s +=  c[i][k]
                ret.append(s)
                s =c[0][j]
        return ret

    def getChr(self, x: str) -> List[str]:
        num = int(x)
        offset = 3 * (num - 2)
        if num<7:
            ret= [chr( 97+offset), chr( 98+offset), chr( 99+offset)]
        elif num==7:
            ret = [chr(97 + offset), chr(98 + offset), chr(99 + offset), chr(100 + offset)]
        elif num == 8:
            offset+=1
            ret = [chr(97 + offset), chr(98 + offset), chr(99 + offset)]
        elif num == 9:
            offset+=1
            ret = [chr(97 + offset), chr(98 + offset), chr(99 + offset), chr(100 + offset)]
        return ret