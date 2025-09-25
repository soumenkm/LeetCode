class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        matrixT = [[None for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                matrixT[i][j] = matrix[j][i]
        return matrixT