class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, n):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            if prices[i] < minPrice:
                minPrice = prices[i]
        
        return maxProfit