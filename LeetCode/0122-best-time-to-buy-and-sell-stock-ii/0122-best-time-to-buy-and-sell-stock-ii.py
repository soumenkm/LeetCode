class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        DP = [[-1 for i in range(2)] for i in range(n)]

        def func(i: int, isBuy: bool) -> int:
            if i == n:
                return 0

            if DP[i][isBuy] != -1:
                return DP[i][isBuy]
            
            if isBuy:
                res = max(-prices[i] + func(i+1, False), 0 + func(i+1, True))
            else:
                res = max(prices[i] + func(i+1, True), 0 + func(i+1, False))
            
            DP[i][isBuy] = res
            return res
        
        res = func(0, True)
        return res