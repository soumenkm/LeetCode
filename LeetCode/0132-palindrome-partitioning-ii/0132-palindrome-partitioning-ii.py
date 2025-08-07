class Solution:
    def minCut(self, s: str) -> int:
        s = list(s)
        n = len(s)
        DP = [-1 for i in range(n)]

        # PDP = [[0 for i in range(n)] for i in range(n)]
        # def isPalin(i: int, j: int) -> bool:
        #     if i >= j:
        #         return True

        #     if s[i] == s[j]:
        #         return isPalin(i+1, j-1)
        #     else:
        #         return False
        
        PDP = [[False for i in range(n)] for i in range(n)]
        for i in range(n):
            PDP[i][i] = True
            if i < n-1:
                PDP[i+1][i] = True
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                # print(i, j)
                # print(PDP)
                if s[i] == s[j]:
                    PDP[i][j] = PDP[i+1][j-1]
                else:
                    PDP[i][j] = False

        def func(i: int) -> int:
            if i == n:
                return 0
            if DP[i] != -1:
                return DP[i]
            res = []
            for j in range(i, n):
                if PDP[i][j]:
                    if j == n-1:
                        temp = func(j+1)
                    else:
                        temp = 1 + func(j+1)
                    res.append(temp)
            DP[i] = min(res)
            return DP[i] 
        
        return func(0)