from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def func(n: int) -> int:
            res = 1
            if n >= 2:
                res = func(n-1) + func(n-2)
            return res
        res = func(n)
        return res