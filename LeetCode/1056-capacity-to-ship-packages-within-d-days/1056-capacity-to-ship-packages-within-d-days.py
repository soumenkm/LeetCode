class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini = max(weights)
        maxi = sum(weights)
        def isPossible(cap: int) -> bool:
            nonlocal days
            load = 0
            totalDays = 0
            for w in weights:
                if load + w <= cap:
                    load += w
                else:
                    totalDays += 1
                    load = w
            if load <= cap:
                totalDays += 1
            return totalDays <= days

        def BS(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if isPossible(mid):
                return BS(low, mid-1)
            else:
                return BS(mid+1, high)
        
        return BS(mini, maxi)