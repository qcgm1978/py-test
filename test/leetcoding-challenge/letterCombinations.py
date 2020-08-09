from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = list(digits)
        c = list(map(self.getChr, l))
        length = len(c)
        if length == 1:
            return c[0]
        try:
            ret=self.getCombinations(c)
        except IndexError:
            return None
        return ret
    def getCombinations(self,c,k=0,ret = []):
        length = len(c)
        if k+1 == length:
            return ret
        if len(ret):
            current = ret
        else:
            current = c[k]
        combi=[]
        for j in range(len(current)):
            for i in range(len(c[k+1])):
                s =current[j]+  c[k+1][i]
                combi.append(s)
        return self.getCombinations(c,k+1,combi)
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