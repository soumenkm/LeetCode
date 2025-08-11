class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1

        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)
        