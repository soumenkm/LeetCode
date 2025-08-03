class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [1 for i in range(n)]
        C = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if 1 + DP[j] > DP[i]:
                        DP[i] = 1 + DP[j]
                        C[i] = C[j]
                    elif 1 + DP[j] == DP[i]:
                        C[i] += C[j]

        maxLen = max(DP)
        res = 0
        for i in range(n):
            if DP[i] == maxLen:
                res = res + C[i]
        
        return res