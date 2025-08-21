class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def LB(low: int, high: int, target) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if target <= nums[mid]:
                return LB(low, mid-1, target)
            else:
                return LB(mid+1, high, target)
        
        def UB(low: int, high: int, target) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if target < nums[mid]:
                return UB(low, mid-1, target)
            else:
                return UB(mid+1, high, target)
        
        n = len(nums)
        lb = LB(0, n-1, target)
        ub = UB(0, n-1, target)
        if lb == ub:
            return [-1, -1]
        else:
            return [lb, ub-1]