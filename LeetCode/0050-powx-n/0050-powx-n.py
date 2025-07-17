class Solution:
    def myPow(self, x: float, n: int) -> float:
        def twosPower(n: int) -> int:
            if n == 0:
                return 1
            else:
                res = twosPower(n-1)
                return res + res
        
        def powerOfTwosMultiple(num: float, n: int, DP: Dict[int, int]) -> float:
            if n in DP:
                return DP[n]
            else:
                if n == 1:
                    res = num
                else:
                    intRes = powerOfTwosMultiple(num, n//2, DP)
                    res = intRes * intRes
                DP[n] = res
                return res
        
        def power(num: float, n: int) -> float:
            N = math.floor(math.log2(n)) + 1
            res = 1.0
            DP = defaultdict(int)
            for i in range(N):
                q, r = divmod(n, 2)
                if r == 1:
                    p2 = twosPower(i)
                    intRes = powerOfTwosMultiple(num, p2, DP)
                    res = res * intRes
                n = q
            return res
     
        if n > 0:
            return power(x, abs(n))
        elif n < 0:
            return 1/power(x, abs(n))
        else:
            return 1
            