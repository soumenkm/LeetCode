class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxCount = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            maxCount = max(count, maxCount)
        return maxCount