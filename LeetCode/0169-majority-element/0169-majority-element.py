class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        n = len(nums)
        for num in nums:
            hashMap[num] += 1
            if hashMap[num] > n // 2:
                return num
