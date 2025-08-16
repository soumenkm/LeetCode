class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        prefixMax = 0
        suffixMax = 0
        res = 0

        while l < r:
            left = height[l]
            right = height[r]
            if left <= right:
                prefixMax = max(prefixMax, left)
                res += prefixMax - left
                l += 1
            else:
                suffixMax = max(suffixMax, right)
                res += suffixMax - right
                r -= 1
            
        return res