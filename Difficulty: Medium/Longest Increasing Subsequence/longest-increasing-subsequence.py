class Solution:
    def lisrec(self, arr):
        n = len(arr)
        DP = [[None for i in range(n+1)] for i in range(n)]
        def func(index: int, prev: int) -> int:
            if index > n-1:
                return 0
            if DP[index][prev+1] is not None:
                return DP[index][prev+1]
                
            lenNotTake = func(index+1, prev) + 0
            lenTake = 0
            if prev == -1 or arr[index] > arr[prev]:
                lenTake = func(index+1, index) + 1
            lenMax = max(lenTake, lenNotTake)
            DP[index][prev+1] = lenMax
            return lenMax
        return func(0, -1)
    
    def lis(self, arr):
        n = len(arr)
        DP = [1 for i in range(n)]
        par = [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i] and DP[j] + 1 > DP[i]:
                    DP[i] = DP[j] + 1
                    par[i] = j
        return max(DP)