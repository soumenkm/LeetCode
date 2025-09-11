
from typing import List


class Solution:
    def countPartitions(self, arr, d):
        
        n = len(arr)
        totalSum = sum(arr)
        if (totalSum - d) % 2 == 1:
            return 0
        if totalSum - d < 0:
            return 0
            
        target = (totalSum - d) // 2
        
        DP = [[-1 for i in range(target+1)] for i in range(n)]
        def func(index: int, target: int) -> int:
            if DP[index][target] != -1:
                return DP[index][target]
            
            if index == 0:
                if arr[0] == 0 and target == 0:
                    res = 2
                    DP[index][target] = res
                    return res
                if target == 0 or arr[0] == target:
                    res = 1
                    DP[index][target] = res
                    return res
                res = 0
                DP[index][target] = res
                return res
            
            resNotTake = func(index-1, target)
            newTarget = target - arr[index]
            resTake = 0
            if newTarget >= 0:
                resTake = func(index-1, newTarget)
            res = resTake + resNotTake
            DP[index][target] = res
            return res
        
        res = func(n-1, target)
        return res
        
        