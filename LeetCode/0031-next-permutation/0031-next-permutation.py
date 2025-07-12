class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                i -= 1
                pivot = nums[i]
                break
        if pivot is None:
            nums.reverse()
        else:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    