#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        n = len(val)
        DP = [[-1 for i in range(capacity+1)] for i in range(n)]
        
        def func(index: int, capacity: int) -> int:
            if DP[index][capacity] != -1:
                return DP[index][capacity]
                
            if index == 0:
                res = (capacity // wt[0]) * val[0]
                DP[index][capacity] = res
                return res
            
            resNotTake = 0 + func(index-1, capacity)
            resTake = 0
            reducedCapacity = capacity - wt[index]
            if reducedCapacity >= 0:
                resTake = val[index] + func(index, reducedCapacity)
            res = max(resTake, resNotTake)
            DP[index][capacity] = res
            return res
        
        res = func(n-1, capacity)
        return res