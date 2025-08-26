class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        jump = 0
        while not (r >= n-1):
            temp = l
            l = r + 1
            for i in range(temp, l):
                r = max(r, i + nums[i])
            jump += 1
        return jump