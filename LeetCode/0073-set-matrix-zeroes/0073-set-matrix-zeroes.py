class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col = [1 for i in range(n)]
        row = [1 for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(m):
            for j in range(n):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0