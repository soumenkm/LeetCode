class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        SDP = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                if j == i:
                    SDP[i][i] = arr[i]
                else:
                    SDP[i][j] = max(SDP[i][j-1], arr[j])
        
        DP = [-1 for i in range(n)]
        def func(i: int) -> int:
            if i == n:
                return 0
            if DP[i] != -1:
                return DP[i]
            res = []
            for j in range(i, i+k):
                if j < n:
                    temp = SDP[i][j] * (j-i+1) + func(j+1)
                    res.append(temp)
            DP[i] = max(res)
            return DP[i]
    
        return func(0)