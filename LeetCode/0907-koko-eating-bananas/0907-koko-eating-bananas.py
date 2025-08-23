class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        def isPossible(k: int) -> bool:
            nonlocal h
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return int(time) <= h

        def BS(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if isPossible(mid):
                return BS(low, mid-1)
            else:
                return BS(mid+1, high)
        
        return BS(1, maxi)