import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=re.match(p,s)
        return m.group()==s if m else False