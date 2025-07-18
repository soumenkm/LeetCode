class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        target = n
        n = 9
        nums = [1,2,3,4,5,6,7,8,9]
        res = []

        def func(index: int, comb: List[int], target: int, k: int):
            if k == 0:
                if target == 0:
                    res.append(comb.copy())
                return
            if index >= n:
                return
            else:
                for i in range(index, n):
                    elem = nums[i]
                    if elem > target:
                        break
                    comb.append(elem)
                    func(i+1, comb, target-elem, k-1)
                    comb.pop()
        
        func(0, [], target, k)
        return res