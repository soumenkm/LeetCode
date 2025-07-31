class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1 = "-" + word1
        s2 = "-" + word2
        m = len(s1)
        n = len(s2)
        DP = [[0 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        
        l = DP[m-1][n-1]
        res = (m-1) + (n-1) - 2 * l
        return res