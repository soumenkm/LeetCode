class Solution:
    def largestDivisibleSubsetTab(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)

        n = len(arr)
        DP = [[0 for i in range(n+1)] for i in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(-1, i):
                resTake = -math.inf
                if j == -1 or arr[i] % arr[j] == 0:
                    resTake = 1 + DP[i+1][i+1]
                DP[i][j+1] = max(DP[i+1][j+1], resTake)
        
        # print(DP)
        
        j = -1
        res = []
        for i in range(n):
            canTake = j == -1 or arr[i] % arr[j] == 0
            resNotTake = DP[i+1][j+1]
            if canTake:
                resTake = 1 + DP[i+1][i+1]
                if resTake > resNotTake:
                    j = i
                    res.append(arr[i])
        # print(res)
        return res
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        n = len(arr)
        DP = [1 for i in range(n)]
        BT = [i for i in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                if arr[i] % arr[j] == 0:
                    if 1 + DP[j] > DP[i]:
                        DP[i] = 1 + DP[j]
                        BT[i] = j
        
        lenLIS = max(DP)
        maxIndex = DP.index(lenLIS)
        index = maxIndex
        res = [arr[index]]
        while BT[index] != index:
            index = BT[index]
            res.append(arr[index])
        
        res.reverse()
        return res

        
        
        
