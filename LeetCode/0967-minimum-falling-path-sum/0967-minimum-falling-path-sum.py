import math
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        # We don't need an extra DP table. We can modify the matrix in-place.
        # We will iterate from the second-to-last row up to the first row.
        # For each cell, we update its value to be itself plus the minimum
        # of the three cells below it.
        
        # Start from the second-to-last row and move upwards.
        for i in range(m - 2, -1, -1):
            for j in range(n):
                # Find the minimum of the three cells in the row below
                
                # Cell directly below
                min_below = matrix[i+1][j]
                
                # Cell below and to the left (if it exists)
                if j > 0:
                    min_below = min(min_below, matrix[i+1][j-1])
                
                # Cell below and to the right (if it exists)
                if j < n - 1:
                    min_below = min(min_below, matrix[i+1][j+1])
                
                # Update the current cell's value
                matrix[i][j] += min_below
                
        # After the loops, the first row of the matrix contains the total
        # minimum path sums for all possible starting points.
        # The answer is the minimum value in this first row.
        return min(matrix[0])