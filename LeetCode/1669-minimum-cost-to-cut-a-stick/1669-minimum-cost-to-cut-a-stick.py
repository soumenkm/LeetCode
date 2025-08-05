class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        arr = range(n+1)
        DP = {}
        def func(i: int, j: int) -> int:
            if j == i + 1:
                return 0
            
            if (i, j) in DP:
                return DP[(i, j)]
            res = []
            for k in cuts:
                if k > i and k < j:
                    resLeft = func(i, k)
                    resRight = func(k, j)
                    tempRes = j - i + resLeft + resRight
                    res.append(tempRes)
                    # print(i, k, j, tempRes, resLeft, resRight)
            res = [r for r in res if r > 0]
            finalRes = min(res) if res else 0
            DP[(i, j)] = finalRes
            return finalRes
        
        return func(0, n)
            