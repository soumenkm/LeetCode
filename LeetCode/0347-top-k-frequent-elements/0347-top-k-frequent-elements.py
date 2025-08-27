class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        maxHeap = []
        count = 0
        for key, val in hashMap.items():
            heapq.heappush(maxHeap, (-val, count, key))
            count += 1
        
        res = []
        for i in range(k):
            _, _, key = heapq.heappop(maxHeap)
            res.append(key)
        
        return res