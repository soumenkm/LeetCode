class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        DP = [[-1 for i in range(2)] for i in range(n)]

        def func(i: int, isBuy: bool) -> int:
            if i >= n:
                return 0
            if DP[i][isBuy] != -1:
                return DP[i][isBuy]

            if isBuy:
                res1 = -prices[i] + func(i+1, False)
                res2 = 0 + func(i+1, True)
            else:
                res1 = prices[i] + func(i+2, True)
                res2 = 0 + func(i+1, False)
            res = max(res1, res2)
            DP[i][isBuy] = res
            return res
        
        return func(0, True)