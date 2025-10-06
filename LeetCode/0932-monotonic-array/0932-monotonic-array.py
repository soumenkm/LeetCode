class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        isInc = True
        isDec = True
        for i in range(1, n):
            if nums[i-1] <= nums[i]:
                isInc = isInc and True 
            else:
                isInc = False
            if nums[i-1] >= nums[i]:
                isDec = isDec and True
            else:
                isDec = False
        return isInc or isDec