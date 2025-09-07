class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        total = nums[0]
        maxLen = 0
        left = 0
        right = 0
        while right < n and left <= right:
            if nums[right] * (right-left+1) <= total + k:
                maxLen = max(maxLen, right-left+1)
                right += 1
                if right < n:
                    total += nums[right]
            else:
                total -= nums[left]
                left += 1

        return maxLen