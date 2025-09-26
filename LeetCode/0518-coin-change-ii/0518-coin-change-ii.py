from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def func(index: int, target: int) -> int:
            if index < 0:
                if target == 0:
                    return 1
                else:
                    return 0
            notTake = func(index-1, target)
            redTarget = target - coins[index]
            take = 0
            if redTarget >= 0:
                take = func(index, redTarget)
            return notTake + take
        
        res = func(len(coins)-1, amount)
        return res