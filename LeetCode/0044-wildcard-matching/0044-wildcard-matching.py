class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        DP = [[-1 for i in range(n)] for i in range(m)]

        def func(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            
            if i >= 0 and j < 0:
                return False
            
            if i < 0 and j >= 0:
                return p[:j+1] == "*" * (j+1)

            if DP[i][j] != -1:
                return DP[i][j]

            if s[i] == p[j] or p[j] == "?":
                res = func(i-1, j-1)
            elif p[j] == "*":
                res = func(i, j-1) or func(i-1, j)
            else:
                res = False
            
            DP[i][j] = res
            return res
        
        return func(m-1, n-1)