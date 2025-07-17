class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        DP = {i: -1 for i in range(-1, n)}
        
        def func(hid: int) -> int:
            if DP[hid] != -1:
                return DP[hid]
            else:
                if hid == -1:
                    res = 0
                elif hid == 0:
                    res = nums[hid]
                else:
                    res1 = func(hid-2) + nums[hid]
                    res2 = func(hid-1)
                    res = max(res1, res2)
                DP[hid] = res
                return res
        
        return func(n-1)