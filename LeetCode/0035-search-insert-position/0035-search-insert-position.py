class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def LB(low: int, high: int, target: int) -> int:
            if low > high:
                return low

            mid = (low + high) // 2
            if target <= nums[mid]:
                res = LB(low, mid - 1, target)
            else:
                res = LB(mid + 1, high, target)
            return res
        return LB(0, n-1, target)