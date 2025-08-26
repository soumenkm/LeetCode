class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda elem: elem[1])
        count = 0
        lastFinish = -math.inf
        for start, finish in intervals:
            if lastFinish <= start:
                count += 1  
                lastFinish = finish
        return len(intervals) - count