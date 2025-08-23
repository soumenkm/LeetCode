class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = math.inf
        def BS(low: int, high: int) -> None:
            nonlocal mini
            if low > high:
                return
            
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                mini = min(mini, nums[mid])
                BS(low, mid-1)
            else:
                mini = min(mini, nums[low])
                BS(mid+1, high)
        
        BS(0, len(nums)-1)
        return mini