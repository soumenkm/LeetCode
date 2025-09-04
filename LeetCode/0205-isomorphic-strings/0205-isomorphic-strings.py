class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}
        n = len(s)
        for i in range(n):
            if s[i] not in mapST:
                mapST[s[i]] = t[i]
            else:
                if mapST[s[i]] != t[i]:
                    return False
            if t[i] not in mapTS:
                mapTS[t[i]] = s[i]
            else:
                if mapTS[t[i]] != s[i]:
                    return False
        return True