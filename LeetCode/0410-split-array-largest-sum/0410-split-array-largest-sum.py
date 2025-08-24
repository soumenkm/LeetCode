class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mini = max(nums)
        maxi = sum(nums)
        def isPossible(arrSum: int) -> bool:
            nonlocal k
            currSum = 0
            numSplit = 0
            for num in nums:
                if currSum + num <= arrSum:
                    currSum += num
                else:
                    numSplit += 1
                    currSum = num
            if currSum <= arrSum:
                numSplit += 1
            return numSplit <= k

        def BS(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if isPossible(mid):
                return BS(low, mid-1)
            else:
                return BS(mid+1, high)
        
        return BS(mini, maxi)