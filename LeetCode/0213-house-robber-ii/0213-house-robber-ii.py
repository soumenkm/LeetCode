class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(nums: List[int]) -> int:
            n = len(nums)
            DP = {i: -1 for i in range(-1, n)}
            DP[-1] = 0 # Base case
            if n >= 1:
                DP[0] = nums[0] # Base case
                for i in range(1, n):
                    DP[i] = max(DP[i-1], DP[i-2] + nums[i])
            return DP[n-1]
        
        n = len(nums)
        res1 = func(nums[1:n-2]) + nums[n-1] # last house is taken
        res2 = func(nums[0:n-1]) # last house is not taken             
        return max(res1, res2)