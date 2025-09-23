class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashMap:
                return [i, hashMap[comp]]
            else:
                hashMap[num] = i
        return []