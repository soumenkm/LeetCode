class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
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
                windowSum += elem % 2
                while windowSum > k:
                    windowSum -= nums[left] % 2
                    left += 1
                windowCount = right - left + 1
                if windowSum <= k:
                    count += windowCount
                right += 1
            return count
        
        res1 = func(k)
        res2 = func(k-1)
        print(res1, res2)
        return res1 - res2