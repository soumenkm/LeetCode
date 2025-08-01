class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1 = "-" + str1
        s2 = "-" + str2
        m = len(s1)
        n = len(s2)
        DP = [[0 for i in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        
        res = []
        def func(i: int, j: int):
            if i == 0 and j == 0:
                return

            if i == 0 and j != 0:
                res.append(s2[j])
                func(i, j-1)
                return
            
            if j == 0 and i != 0:
                res.append(s1[i])
                func(i-1, j)
                return
            
            if s1[i] == s2[j]:
                res.append(s1[i])
                func(i-1, j-1)
            else:
                if DP[i][j-1] > DP[i-1][j]:
                    res.append(s2[j])
                    func(i, j-1)
                else:
                    res.append(s1[i])
                    func(i-1, j)
        
        func(m-1, n-1)
        res.reverse()
        return "".join(res)