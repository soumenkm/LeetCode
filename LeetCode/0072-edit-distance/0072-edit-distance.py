class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        DP = [[-1 for i in range(n)] for i in range(m)]

        def func(i: int, j: int) -> int:
            if i < 0:
                return j+1
            if j < 0:
                return i+1

            if DP[i][j] != -1:
                return DP[i][j]

            if word1[i] == word2[j]:
                res = func(i-1, j-1)
            else:
                resInsert = 1 + func(i, j-1)
                resDelete = 1 + func(i-1, j)
                resReplace = 1 + func(i-1, j-1)
                res = min(resInsert, resDelete, resReplace)
            
            DP[i][j] = res
            return res
        
        return func(m-1, n-1)