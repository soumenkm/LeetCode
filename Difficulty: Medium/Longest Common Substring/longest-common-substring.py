#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        s1 = "0" + s1
        s2 = "0" + s2
        m = len(s1)
        n = len(s2)
        
        DP = [[0 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    DP[i][j] = 1 + DP[i-1][j-1]
        
        return max([max(DP[i]) for i in range(m)])