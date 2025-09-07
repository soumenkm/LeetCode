import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def partition(low: int, high: int) -> int:
        #     pivotIndex = low
        #     pivot = nums[pivotIndex]
        #     last = high
        #     while low <= high <= last:
        #         if nums[low] > pivot:
        #             nums[low], nums[high] = nums[high], nums[low]
        #         else:
        #             low += 1
        #             continue
                
        #         if nums[high] < pivot:
        #             nums[low], nums[high] = nums[high], nums[low]
        #         elif nums[high] >= pivot:
        #             high -= 1
            
        #     nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]
        #     return high
    
        # def partition(low: int, high: int) -> int:
        #     pivot = nums[high]
        #     i = low
        #     for j in range(low, high):
        #         if nums[j] <= pivot:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #     nums[i], nums[high] = nums[high], nums[i]
        #     return i

        # def quickSort(low: int, high: int) -> None:
        #     if low >= high:
        #         return
        
        #     mid = partition(low, high)
        #     quickSort(low, mid-1)
        #     quickSort(mid+1, high)
        
        # quickSort(0, len(nums)-1)
        # return nums
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            m = len(left)
            n = len(right)
            i = 0
            j = 0
            res = []
            while i < m and j < n:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i == m:
                for k in range(j, n):
                    res.append(right[k])
            elif j == n:
                for k in range(i, m):
                    res.append(left[k])
            return res

        def mergeSort(low: int, high: int) -> List[int]:
            if low == high:
                return [nums[low]]

            mid = (low + high) // 2
            left = mergeSort(low, mid)
            right = mergeSort(mid+1, high)
            comb = merge(left, right)
            return comb
        
        return mergeSort(0, len(nums) - 1)