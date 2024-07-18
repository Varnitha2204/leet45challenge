import re
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        x = s.split(':')
        y = re.findall(r'\d+',s)
        z = list(map(int,y))
        a = re.findall(r"[a-zA-Z]+",s)
        b,c = ord(a[0]),ord(a[-1])
        l = []
        for i in range(b,c+1):
            for j in range(z[0],z[1]+1):
                l.append(chr(i)+str(j))
        return l
