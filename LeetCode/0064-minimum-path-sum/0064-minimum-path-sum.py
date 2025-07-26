class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        DP = [[-1 for _ in range(n)] for _ in range(m)]
        DP[0][0] = grid[0][0]
        
        for i in range(1, m):
            DP[i][0] = grid[i][0] + DP[i-1][0]
        for j in range(1, n):
            DP[0][j] = grid[0][j] + DP[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
        
        return DP[m-1][n-1]