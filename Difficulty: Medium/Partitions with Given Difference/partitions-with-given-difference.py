
from typing import List


class Solution:
    def countPartitions(self, arr, d):
        # code here
        n = len(arr)
        t, rem = divmod((sum(arr) - d), 2)
        if t < 0 or rem == 1:
            return 0
      
        DP = [[None for i in range(t+1)] for j in range(n)]
        for j in range(t+1):
            DP[0][j] = int(arr[0] == j)
        DP[0][0] += 1
        
        for i in range(1, n):
            for j in range(t+1):
                rt = j - arr[i]
                take = 0
                if rt >= 0:
                    take = DP[i-1][rt]
                notTake = DP[i-1][j]
                DP[i][j] = take + notTake
        
        return DP[n-1][t]
