class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                val = candidates[index]
                comb.append(val)
                func(index, comb, target - val)
                comb.pop()
                func(index+1, comb, target)
        
        func(0, [], target)
        return res

            
