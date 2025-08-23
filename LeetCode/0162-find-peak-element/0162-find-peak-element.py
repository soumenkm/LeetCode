class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        if n == 1:
            return 0

        def BS(low: int, high: int) -> int:
            nonlocal n
            mid = (low + high) // 2
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return mid
            if mid == n-1:
                if arr[mid] > arr[mid-1]:
                    return mid

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid] < arr[mid+1]:
                return BS(mid+1, high)
            if arr[mid] > arr[mid+1]:
                return BS(low, mid-1)
        
        return BS(0, n-1)