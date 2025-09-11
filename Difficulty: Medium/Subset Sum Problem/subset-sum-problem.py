class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        DP = [[-1 for i in range(sum+1)] for j in range(n)]
        
        def func(index: int, target: int) -> bool:
            if DP[index][target] != -1:
                return DP[index][target]
            
            if target == 0:
                res = True
                DP[index][target] = res
                return res
            if index == 0:
                res = target == arr[index]
                DP[index][target] = res
                return res
            
            res1 = func(index-1, target)
            res2 = False
            newTarget = target-arr[index]
            if newTarget >= 0:
                res2 = func(index-1, newTarget)
            res = res1 or res2
            DP[index][target] = res
            return res
            
        return func(n-1, sum)
        