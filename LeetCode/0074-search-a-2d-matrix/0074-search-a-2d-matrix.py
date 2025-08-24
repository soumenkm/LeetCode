class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def BS(low: int, high: int, target: int) -> bool:
            nonlocal n

            if low > high:
                return False
            
            mid = (low + high) // 2
            row, col = divmod(mid, n)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                return BS(low, mid-1, target)
            else:
                return BS(mid+1, high, target)

        return BS(0, m * n - 1, target)