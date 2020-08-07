class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = []
        for i in range(numRows):
            l.append([])
        j=0
        for i in range(len(s)):
            l[j].append(s[i])
            length=len(l[j])
            if j>0 and length != len(l[j - 1]):
                for n in range(numRows):
                    if n != j:
                        l[n].append('')
            if j == numRows-1:
                j-=1
            elif j==0 or l[j - 1][-1]:
                j += 1
            else:
                j -= 1
        ret=''
        for i in range(numRows):
            ret+=''.join(l[i])
        return ret