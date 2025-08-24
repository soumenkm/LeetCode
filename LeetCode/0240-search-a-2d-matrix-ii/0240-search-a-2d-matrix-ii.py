class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0 
        col = n-1

        while not (row == m or col == -1):
            print(row, col)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col = col - 1
            elif target > matrix[row][col]:
                row = row + 1
        
        return False