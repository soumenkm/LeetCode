class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(low: int, high: int, target: int) -> int:
            if low > high:
                return -1
            
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    return BS(mid+1, high, target)
                else:
                    return BS(low, mid-1, target)
            else:
                if nums[low] <= target < nums[mid]:
                    return BS(low, mid-1, target)
                else:
                    return BS(mid+1, high, target)
        
        n = len(nums)
        return BS(0, n-1, target)