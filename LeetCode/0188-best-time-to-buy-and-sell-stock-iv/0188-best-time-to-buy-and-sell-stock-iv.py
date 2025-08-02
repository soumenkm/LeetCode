class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        DP = [[[-1 for i in range(k+1)] for i in range(2)] for i in range(n)]

        def func(i: int, isBuy: bool, cap: int) -> int:
            if cap == 0:
                return 0
            if i == n:
                return 0
            
            if DP[i][isBuy][cap] != -1:
                return DP[i][isBuy][cap]

            if isBuy:
                res1 = -prices[i] + func(i+1, False, cap)
                res2 = 0 + func(i+1, True, cap)
                res = max(res1, res2)
            else:
                res1 = prices[i] + func(i+1, True, cap-1)
                res2 = 0 + func(i+1, False, cap)
                res = max(res1, res2)

            DP[i][isBuy][cap] = res
            return res 
    
        return func(0, True, k)