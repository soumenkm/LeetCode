class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap = defaultdict(int)
        preMap[0] = 1
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            targetSum = prefixSum - k
            if targetSum in preMap:
                count += preMap[targetSum]
            preMap[prefixSum] += 1
        return count