class Solution:
    def fib(self, n: int) -> int:
        DP = [0] * (n+1)
        def func(n: int) -> int:
            if n == 0:
                res = 0
            elif n == 1:
                res = 1
            else:
                res = func(n-1) + func(n-2)
            DP[n] = res
            return res
        
        return func(n)