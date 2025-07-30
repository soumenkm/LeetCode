class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        DP = [[-1 for i in range(m)] for i in range(n)]

        def func(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if DP[i][j] != -1:
                return DP[i][j]

            if text1[i] == text2[j]:
                res = 1 + func(i-1, j-1)
            else:
                res1 = func(i, j-1)
                res2 = func(i-1, j)
                res = max(res1, res2)
            
            DP[i][j] = res
            return res
        
        res = func(n-1, m-1)
        return res