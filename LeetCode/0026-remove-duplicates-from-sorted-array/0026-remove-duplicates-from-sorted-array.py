class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
                i += 1
        return j + 1