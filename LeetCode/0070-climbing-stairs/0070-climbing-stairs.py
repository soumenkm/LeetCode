class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [-1 for i in range(n+1)]
        def func(n: int) -> int:
            if DP[n] != -1:
                return DP[n]
            else:
                res = 1
                if n >= 2:
                    res = func(n-1) + func(n-2)
                DP[n] = res
                return res
        res = func(n)
        return res