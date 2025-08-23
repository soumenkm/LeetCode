class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        if n == 1:
            return arr[0]

        def BS(low: int, high: int) -> int:
            nonlocal n
            mid = (low + high) // 2
            if mid == 0:
                if arr[mid] != arr[mid+1]:
                    return arr[mid]
            if mid == n-1:
                if arr[mid] != arr[mid-1]:
                    return arr[mid]
            if arr[mid-1] != arr[mid] and arr[mid] != arr[mid+1]:
                return arr[mid]
            
            if mid % 2 == 1 and arr[mid] == arr[mid-1]:
                return BS(mid+1, high)
            if mid % 2 == 1 and arr[mid] == arr[mid+1]:
                return BS(low, mid-1)
            if mid % 2 == 0 and arr[mid] == arr[mid+1]:
                return BS(mid+1, high)
            if mid % 2 == 0 and arr[mid] == arr[mid-1]:
                return BS(low, mid-1)

        return BS(0, n-1)