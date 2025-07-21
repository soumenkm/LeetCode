class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]

        res = []
        def func(index: int, perm: List[int], indexSet: Set[int]) -> bool:
            nonlocal k
            if index == n:
                res.append(perm.copy())
                k = k - 1
                if k == 0:
                    return True
                else:
                    return False
            
            for i in range(n):
                if i not in indexSet:
                    elem = nums[i]
                    perm.append(elem)
                    indexSet.add(i)
                    
                    if func(index+1, perm, indexSet):
                        return True
                    
                    perm.pop()
                    indexSet.remove(i)
            
            return False
        
        func(0, [], set())
        return "".join([str(i) for i in res[-1]])