class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        DP = [[-1 for i in range(n)] for i in range(m)]
        def func(i: int, j: int) -> int:
            if j < 0:
                return 1
            if i < 0:
                return 0

            if DP[i][j] != -1:
                return DP[i][j]

            if s[i] == t[j]:
                res1 = func(i-1, j-1)
                res2 = func(i-1, j)
                res = res1 + res2
            else:
                res = func(i-1, j)
            
            DP[i][j] = res
            return res

        return func(m-1, n-1)