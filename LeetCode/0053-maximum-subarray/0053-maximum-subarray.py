class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # DP = [None for i in range(n)]
        # DP[0] = nums[0]
        # for i in range(1, len(nums)):
        #     DP[i] = max(nums[i], nums[i] + DP[i-1])
        # return max(DP)

        currSum = 0
        maxSum = -math.inf
        for num in nums:
            currSum = currSum + num
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum