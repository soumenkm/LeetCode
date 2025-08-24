class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxi = max(nums)
        mini = 1
        def isPossible(div: int) -> bool:
            nonlocal threshold
            total = 0
            for num in nums:
                total += math.ceil(num / div)
            return total <= threshold
        
        def BS(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if isPossible(mid):
                return BS(low, mid-1)
            else:
                return BS(mid+1, high)
        
        return BS(mini, maxi)