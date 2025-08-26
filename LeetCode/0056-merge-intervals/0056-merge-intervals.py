class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda elem: elem[0])
        prevStart, prevFinish = intervals[0]
        merge = []
        for start, finish in intervals[1:]:
            if start <= prevFinish:
                prevFinish = max(prevFinish, finish)
            else:
                merge.append([prevStart, prevFinish])
                prevStart, prevFinish = start, finish
        merge.append([prevStart, prevFinish])
        return merge