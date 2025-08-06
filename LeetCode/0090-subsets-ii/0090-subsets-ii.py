class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []

        def func(index: int, subset: List[int]):
            if index >= n:
                res.append(subset.copy())
                return
            else:
                for i in range(index, n):
                    if not (i > index and nums[i] == nums[i-1]):
                        elem = nums[i]
                        subset.append(elem)
                        func(i+1, subset)
                        subset.pop()
                res.append(subset.copy())
        
        func(0, [])
        return res