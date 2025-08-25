class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = 0
        si = 0
        sn = len(s)
        gn = len(g)
        while not (si == sn or gi == gn):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi