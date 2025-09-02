class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        numSubsets = 1 << n
        res = []
        for i in range(numSubsets):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            res.append(subset)
        return res

    def subsetsRec(self, nums: List[int]) -> List[List[int]]:
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

    def subsetsParameter(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def func(idx: int, currentSubseq: List[int]):
            if idx >= n:
                res.append(currentSubseq.copy())
            else:
                currentSubseq.append(nums[idx])
                func(idx+1, currentSubseq)
                currentSubseq.pop()
                func(idx+1, currentSubseq)
        func(0, [])
        return res