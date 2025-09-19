from functools import cache
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        @cache
        def mcm(i: int, j: int) -> int:
            if j-i == 1:
                return 0
                
            mini = float("inf")
            for k in range(i+1, j):
                mult = mcm(i, k) + mcm(k, j) + arr[i] * arr[j] * arr[k]
                mini = min(mini, mult)
            return mini
        
        return mcm(0, n-1)