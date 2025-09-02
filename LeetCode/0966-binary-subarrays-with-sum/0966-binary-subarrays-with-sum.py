class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            right = 0
            count = 0
            windowSum = 0
            n = len(nums)
            while right < n:
                elem = nums[right]
                windowSum += elem
                while windowSum > k:
                    windowSum -= nums[left]
                    left += 1
                windowCount = right - left + 1
                if windowSum <= k:
                    count += windowCount
                right += 1
            return count
        
        res1 = func(goal)
        res2 = func(goal-1)
        print(res1, res2)
        return res1 - res2