class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        target = s//2
        n = len(nums)
        DP = [[-1 for i in range(target+1)] for j in range(n)]

        def func(index: int, target: int) -> bool:
            if DP[index][target] != -1:
                return DP[index][target]

            if target == 0:
                res = True
                DP[index][target] = res
                return res
            
            if index == 0:
                res = nums[index] == target
                DP[index][target] = res
                return res

            res1 = func(index-1, target)
            newTarget = target-nums[index]
            res2 = False
            if newTarget >= 0:
                res2 = func(index-1, newTarget)
            res = res1 or res2
            DP[index][target] = res
            return res
        
        res = func(n-1, target)
        return res

            

