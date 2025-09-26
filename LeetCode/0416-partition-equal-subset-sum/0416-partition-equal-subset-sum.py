class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def func(arr: List[int], target: int) -> bool:
            n = len(arr)
            DP = [[None for i in range(target+1)] for i in range(n)]
            for i in range(target+1):
                DP[0][i] = (i == arr[0])
            DP[0][0] = True

            for i in range(1, n):
                for j in range(target+1):
                    resNotTake = DP[i-1][j]
                    resTake = False
                    redTarget = j - arr[i]
                    if redTarget >= 0:
                        resTake = DP[i-1][redTarget]
                    DP[i][j] = resTake or resNotTake
            
            return DP[n-1][target]
        
        target, rem = divmod(sum(nums), 2)
        if rem == 1:
            return False
        else:
            return func(nums, target)