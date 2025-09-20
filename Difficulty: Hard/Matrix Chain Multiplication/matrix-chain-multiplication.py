from functools import cache
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        @cache
        def func(i: int, j: int) -> int:
            if j - i == 1:
                return 0
            
            mini = float("inf")
            for k in range(i+1, j):
                mult = func(i, k) + func(k, j) + arr[i] * arr[k] * arr[j]
                mini = min(mini, mult)
            
            return mini
        
        return func(0, len(arr) - 1)
            
        
        