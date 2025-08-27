class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        
        if self.left and self.right and -self.left[0] > self.right[0]:
            top = -heapq.heappop(self.left)
            heapq.heappush(self.right, top)
        
        if self.left and len(self.left) > len(self.right) + 1:
            top = -heapq.heappop(self.left)
            heapq.heappush(self.right, top)
        
        if self.right and len(self.right) > len(self.left) + 1:
            top = heapq.heappop(self.right)
            heapq.heappush(self.left, -top)

    def findMedian(self) -> float:
        m = len(self.left)
        n = len(self.right)
        maxElem = -self.left[0] if m > 0 else None
        minElem = self.right[0] if n > 0 else None
        if m == n:
            med = (maxElem + minElem) / 2
        elif m > n:
            med = maxElem
        elif m < n:
            med = minElem
        return med
        

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()