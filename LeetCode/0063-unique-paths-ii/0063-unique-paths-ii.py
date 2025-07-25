class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP = [[-1 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                DP[i][0] = 1
            else:
                for j in range(i, m):
                    DP[j][0] = 0
                break
            
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                DP[0][i] = 1
            else:
                for j in range(i, n):
                    DP[0][j] = 0
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
                else:
                    DP[i][j] = DP[i][j-1] + DP[i-1][j]
        
        return DP[m-1][n-1]