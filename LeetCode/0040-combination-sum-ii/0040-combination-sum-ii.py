class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        
        def func(index: int, comb: List[int], target: int):
            if target == 0:
                res.append(comb.copy())
                return
            elif target < 0:
                return
            
            if index >= n:
                return
            else:
                for i in range(index, n):
                    if not (i > index and candidates[i] == candidates[i-1]):
                        elem = candidates[i]
                        comb.append(elem)
                        func(i+1, comb, target-elem)
                        comb.pop()
        
        func(0, [], target)
        return res