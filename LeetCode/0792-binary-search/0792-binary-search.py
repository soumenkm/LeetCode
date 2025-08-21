class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def func(i: int, j: int, target: int) -> int:
            if i > j:
                return -1
            
            div = (i + j) // 2
            if target == nums[div]:
                res = div
            elif target < nums[div]:
                res = func(i, div - 1, target)
            elif target > nums[div]:
                res = func(div + 1, j, target)
            return res
        res = func(0, len(nums)-1, target)
        return res