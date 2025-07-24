class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[-1 for j in range(n)] for i in range(m)]
        for j in range(n):
            DP[0][j] = 1 # Base case
        for i in range(m):
            DP[i][0] = 1 # Base case
            
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i][j-1] + DP[i-1][j]
        return DP[m-1][n-1]