class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def countPairs(left: List[int], right: List[int]) -> int:
            n1 = len(left)
            n2 = len(right)
            if n1 <= 0 or n2 <= 0:
                return 0
            
            count = 0
            i = 0
            j = 0
            while i < n1 and j < n2:
                if left[i] > 2 * right[j]:
                    count += (n1 - i)
                    j += 1
                else:
                    i += 1

            return count
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            n1 = len(left)
            n2 = len(right)
            if n1 <= 0 and n2 > 0:
                return right
            if n1 > 0 and n2 <= 0:
                return left
            if n1 <= 0 and n2 <= 0:
                return []
            
            i = 0
            j = 0
            res = []
            while i < n1 and j < n2:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            if i == n1 and j < n2:
                for k in range(j, n2):
                    res.append(right[k])
            elif i < n1 and j == n2:
                for k in range(i, n1):
                    res.append(left[k])
            
            return res

        totalCount = 0
        def mergeSort(start: int, end: int) -> List[int]:
            nonlocal totalCount
            if start == end:
                return [nums[start]]
            
            mid = (start + end) // 2
            leftSorted = mergeSort(start, mid)
            rightSorted = mergeSort(mid+1, end)
            sortedArr = merge(leftSorted, rightSorted)
            pairs = countPairs(leftSorted, rightSorted)
            totalCount += pairs
    
            return sortedArr

        mergeSort(0, len(nums)-1)
        return totalCount