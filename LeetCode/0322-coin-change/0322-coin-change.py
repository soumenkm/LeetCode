from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def func(index: int, target: int) -> int:
            if target == 0:
                return 0

            if index < 0:
                return float("inf")

            notTake = func(index-1, target)
            take = float("inf")
            redTgt = target - coins[index]
            if redTgt >= 0:
                take = 1 + func(index, redTgt) 
            return min(notTake, take)
            
        res = func(len(coins)-1, amount)
        if res == float("inf"):
            return -1
        else:
            return res