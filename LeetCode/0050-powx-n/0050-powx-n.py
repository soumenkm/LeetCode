class Solution:
    def myPow(self, x: float, n: int) -> float:
        def twosPower(n: int) -> int:
            if n == 0:
                return 1
            else:
                res = twosPower(n-1)
                return res + res
        
        def powerOfTwosMultiple(num: float, n: int) -> float:
            if n == 0:
                return 1.0
            elif n == 1:
                return num
            else:
                res = powerOfTwosMultiple(num, n//2)
                comb = res * res
                return comb
        
        def power(num: float, n: int) -> float:
            N = math.floor(math.log2(n)) + 1
            res = 1.0
            for i in range(N):
                q, r = divmod(n, 2)
                if r == 1:
                    p2 = twosPower(i)
                    res = res * powerOfTwosMultiple(num, p2)
                n = q
            return res
     
        if n > 0:
            return power(x, abs(n))
        elif n < 0:
            return 1/power(x, abs(n))
        else:
            return 1
            