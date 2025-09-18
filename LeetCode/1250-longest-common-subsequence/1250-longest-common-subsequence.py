class Solution:
    def longestCommonSubsequenceOld(self, text1: str, text2: str) -> int:
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

    








    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        DP = [[None for i in range(n)] for i in range(m)]

        def func(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            
            if DP[i][j] is not None:
                return DP[i][j]

            resMatch, resNotMatch = 0, 0
            if text1[i] == text2[j]:
                resMatch = 1 + func(i-1, j-1)
            else:
                resNotMatch = max(func(i-1, j), func(i, j-1))
            
            res = max(resMatch, resNotMatch)
            DP[i][j] = res
            return res

        return func(m-1, n-1)
