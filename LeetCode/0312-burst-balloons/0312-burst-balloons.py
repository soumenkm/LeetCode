class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        DP = [[-1 for i in range(n)] for i in range(n)]

        def func(i: int, j: int) -> int:
            if j == i + 1:
                return 0
            if DP[i][j] != -1:
                return DP[i][j]
            res = []
            for k in range(i+1, j):
                intRes = nums[i] * nums[j] * nums[k] + func(i, k) + func(k, j)
                res.append(intRes)

            DP[i][j] = max(res)
            return DP[i][j]
        
        return func(0, n-1)