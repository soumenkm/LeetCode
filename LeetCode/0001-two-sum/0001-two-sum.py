class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash_map:
                return [i, hash_map[comp]]
            else:
                hash_map[num] = i
        return []

        