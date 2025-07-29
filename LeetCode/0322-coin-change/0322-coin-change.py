class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        DP = [[-1 for i in range(amount+1)] for i in range(n)]

        def func(index: int, amount: int) -> int:
            if DP[index][amount] != -1:
                return DP[index][amount]
            
            if index == 0:
                res, rem = divmod(amount, coins[index])
                if rem == 0:
                    DP[index][amount] = res
                    return res
                else:
                    DP[index][amount] = math.inf
                    return math.inf
                
            resNotTake = func(index-1, amount)
            reducedAmount = amount - coins[index]
            resTake = math.inf
            if reducedAmount >= 0:
                resTake = 1 + func(index, reducedAmount)

            res = min(resTake, resNotTake)
            DP[index][amount] = res
            return res
        
        res = func(n-1, amount)
        return res if res != math.inf else -1
