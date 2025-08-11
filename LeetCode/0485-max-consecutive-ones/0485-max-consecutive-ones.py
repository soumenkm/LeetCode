class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cons = cons + 1
            if nums[i] == 0:
                maxi = max(maxi, cons)
                cons = 0
        
        maxi = max(maxi, cons)
        return maxi