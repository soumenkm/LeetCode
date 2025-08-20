class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def func(i: int, j: int, target: int) -> int:
            if i >= j:
                if nums[i] == target:
                    return i
                else:
                    return -1
            
            div = (i + j) // 2
            if target < nums[div]:
                res = func(i, div, target)
            elif target > nums[div]:
                res = func(div + 1, j, target)
            else:
                res = div
            return res
        res = func(0, len(nums)-1, target)
        return res