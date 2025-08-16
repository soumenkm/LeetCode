class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr = heights
        n = len(arr)
        pse = [(-1, -1) for i in range(n)]
        nse = [(-1, n) for i in range(n)]
        stack = []
        for i in range(n):
            while stack and arr[i] < stack[-1][0]:
                top = stack.pop()
                nse[top[1]] = (arr[i], i)
            if stack:
                pse[i] = stack[-1]
            stack.append((arr[i], i))
        
        res = 0
        for i in range(n):
            intRes = arr[i] * (nse[i][1] - pse[i][1] - 1)
            res = max(res, intRes)
        
        return res