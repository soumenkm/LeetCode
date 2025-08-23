class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        mini = min(bloomDay)
        maxi = max(bloomDay)
        def isPossible(day: int) -> bool:
            nonlocal m
            nonlocal k
            n = len(bloomDay)
            count = 0
            currM = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    currM += count // k
                    count = 0
            currM += count // k
            return currM >= m
        
        def BS(low: int, high: int) -> int:
            if low > high:
                return low
            
            mid = (low + high) // 2
            if isPossible(mid):
                return BS(low, mid-1)
            else:
                return BS(mid+1, high)
        
        if m * k > len(bloomDay):
            return -1
        
        return BS(mini, maxi)