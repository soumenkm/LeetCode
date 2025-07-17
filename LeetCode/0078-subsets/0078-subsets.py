class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def func(idx: int) -> List[List[int]]:
            if idx >= n:
                return [[]]
            else:
                res = func(idx+1) # [[], [2], [3], [2,3]]
                combinedRes = []
                for r in res:
                    combinedRes.append(r)
                    combinedRes.append([nums[idx]] + r)
                return combinedRes
        return func(0)
