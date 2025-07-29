class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        maxRange =  abs(target) + totalSum
        minRange = -(abs(target) + totalSum) 
        DP = [{i: -1 for i in range(minRange, maxRange+1)} for i in range(n)]

        def func(index: int, target: int) -> int:
            if DP[index][target] != -1:
                return DP[index][target]
            
            if index == 0:
                if nums[0] == 0 and target == 0:
                    DP[index][target] = 2
                    return 2
                if abs(target) == nums[0]:
                    DP[index][target] = 1
                    return 1
                DP[index][target] = 0
                return 0

            newNegTarget = target + nums[index]
            newPosTarget = target - nums[index]
            resNeg = 0
            if minRange <= newNegTarget <= maxRange:
                resNeg = func(index-1, newNegTarget)
            resPos = 0
            if minRange <= newPosTarget <= maxRange:
                resPos = func(index-1, newPosTarget)
            res = resPos + resNeg
            DP[index][target] = res
            return res

        res = func(n-1, target)
        return res