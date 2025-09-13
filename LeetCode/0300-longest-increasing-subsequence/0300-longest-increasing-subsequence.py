class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [[-1 for i in range(n+1)] for i in range(n)]
        def func(index: int, prev: int) -> int:
            if index == n:
                return 0
            if DP[index][prev+1] != -1:
                return DP[index][prev+1] 
            resNotTake = func(index+1, prev)
            resTake = -math.inf
            if prev == -1 or nums[index] > nums[prev]:
                resTake = 1 + func(index+1, index)
            res = max(resTake, resNotTake)
            DP[index][prev+1] = res
            return res
        return func(0, -1)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], 1 + DP[j])
        
        return max(DP)