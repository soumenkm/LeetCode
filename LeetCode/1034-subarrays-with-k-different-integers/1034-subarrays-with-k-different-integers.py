class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def func(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            right = 0
            count = 0
            n = len(nums)
            hashMap = defaultdict(int)

            while right < n:
                hashMap[nums[right]] += 1
                while len(hashMap) > k:
                    hashMap[nums[left]] -= 1
                    if hashMap[nums[left]] == 0:
                        hashMap.pop(nums[left])
                    left += 1
                
                windowCount = right - left + 1
                count += windowCount
                right += 1

            return count
        
        res1 = func(k)
        res2 = func(k-1)
        return res1 - res2