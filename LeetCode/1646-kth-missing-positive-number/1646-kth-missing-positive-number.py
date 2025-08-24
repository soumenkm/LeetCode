class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = []
        n = len(arr)
        for i in range(n):
            nums.append(arr[i] - (i+1))
        
        def LB(low: int, high: int, target: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if target <= nums[mid]:
                return LB(low, mid-1, target)
            else:
                return LB(mid+1, high, target)
        
        lb = LB(0, n-1, k)
        return lb + k