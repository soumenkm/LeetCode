class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = -math.inf
        for i in range(n):
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-1-i]
            res = max(res, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        
        return res
