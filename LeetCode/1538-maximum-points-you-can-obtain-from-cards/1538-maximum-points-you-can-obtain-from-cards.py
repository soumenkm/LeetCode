class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = k - 1

        maxSum = 0
        for i in range(left, right+1):
            maxSum += cardPoints[i]
        
        left = n-1
        currSum = maxSum
        while right > -1:
            currSum -= cardPoints[right]
            right -= 1
            currSum += cardPoints[left]
            left -= 1
            maxSum = max(maxSum, currSum)
        
        return maxSum