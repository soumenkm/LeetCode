class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        ans = start ^ goal
        count = 0
        while ans > 0:
            ans, rem = divmod(ans, 2)
            count += rem
        return count