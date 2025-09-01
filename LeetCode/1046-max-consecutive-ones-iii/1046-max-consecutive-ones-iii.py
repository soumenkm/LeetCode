class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        maxLen = 0
        
        while right < n:
            currLen = right - left + 1
            if nums[right] == 0:
                zeros += 1

            if zeros <= k:
                maxLen = max(maxLen, currLen)
            else:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            right += 1
        
        return maxLen