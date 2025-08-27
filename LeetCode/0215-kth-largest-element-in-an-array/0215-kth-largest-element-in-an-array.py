class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap)
        for num in nums[k:]:
            if num > minheap[0]: 
                heapq.heapreplace(minheap, num)
        return minheap[0]