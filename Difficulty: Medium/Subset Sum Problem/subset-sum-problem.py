from functools import cache
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        # @cache
        # def func(index: int, target: int) -> bool:
        #     if target == 0:
        #         return True
            
        #     if index < 0:
        #         return False
            
        #     notTake = func(index-1, target)
        #     if notTake:
        #         return notTake
                
        #     take = False
        #     reducedTarget = target - arr[index]
        #     if reducedTarget >= 0:
        #         take = func(index-1, reducedTarget)
        #     res = take or notTake
        #     return res
        
        # return func(len(arr)-1, sum)
        
        target = sum
        n = len(arr)
        DP = [[None for i in range(target+1)] for i in range(n)]
        for j in range(target+1):
            DP[0][j] = (arr[0] == j)
        DP[0][0] = True
        
        for i in range(1, n):
            for j in range(target+1):
                notTake = DP[i-1][j]
                take = False
                reducedTarget = j - arr[i]
                if reducedTarget >= 0:
                    take = DP[i-1][reducedTarget]
                DP[i][j] = take or notTake
        
        return DP[n-1][target]
        