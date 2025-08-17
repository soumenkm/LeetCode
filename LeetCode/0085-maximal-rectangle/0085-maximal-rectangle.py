class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        arr = [[0 for i in range(n)] for i in range(m)]
        for j in range(n):
            arr[0][j] = int(matrix[0][j])
            for i in range(1, m):
                if matrix[i][j] == "1":
                    arr[i][j] = arr[i-1][j] + int(matrix[i][j])
        
        def maxRectHist(arr: List[int]) -> int:
            n = len(arr)
            stack = []
            pse = [(-1, -1) for i in range(n)]
            nse = [(-1, n) for i in range(n)]
            for i in range(n):
                while stack and arr[i] < stack[-1][0]:
                    nse[stack[-1][1]] = (arr[i], i)
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                stack.append((arr[i], i))
            
            totalArea = 0
            for i in range(n):
                area = (nse[i][1] - pse[i][1] - 1) * arr[i]
                totalArea = max(totalArea, area)
            
            return totalArea

        totalArea = 0
        for i in range(m):
            area = maxRectHist(arr[i])
            totalArea = max(totalArea, area)
        
        return totalArea