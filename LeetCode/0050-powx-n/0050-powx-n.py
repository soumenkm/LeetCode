class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(x: float, n: int) -> float:
            if n == 0:
                return 1
            elif n > 0:
                return x * func(x, n-1)
            elif n < 0:
                return 1/x * func(x, n+1)
        # return func(x, n)
        return x ** n