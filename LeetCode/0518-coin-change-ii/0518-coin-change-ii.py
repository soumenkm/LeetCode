class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        DP = [[-1 for i in range(amount+1)] for i in range(n)]

        def func(index: int, amount: int) -> int:
            if DP[index][amount] != -1:
                return DP[index][amount]

            if index == 0:
                res, rem = divmod(amount, coins[index])
                if rem == 0:
                    DP[index][amount] = 1
                    return 1
                else:
                    DP[index][amount] = 0
                    return 0
            
            resNotTake = func(index-1, amount)
            resTake = 0
            reducedAmount = amount - coins[index]
            if reducedAmount >= 0:
                resTake = func(index, reducedAmount)
            res = resTake + resNotTake
            DP[index][amount] = res
            return res
    
        res = func(n-1, amount)
        return res