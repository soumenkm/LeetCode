class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        n = len(nums)
        for i in range(n):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= n-1:
                return True