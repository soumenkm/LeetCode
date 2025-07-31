class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = "-" + s
        s = s[::-1]
        s2 = "-" + s

        m = len(s1)
        n = len(s2)
        DP = [[0 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
 
        return DP[m-1][n-1]