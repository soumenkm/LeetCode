class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        def findMax(colIndex: int) -> Tuple[int, int]:
            nonlocal m
            maxi = mat[0][colIndex]
            maxiIndex = 0
            for i in range(1, m):
                if mat[i][colIndex] > maxi:
                    maxi = mat[i][colIndex]
                    maxiIndex = i
            return maxi, maxiIndex

        def BS(low: int, high: int) -> List[int]:
            mid = (low + high) // 2
            maxi, maxiIndex = findMax(mid)

            rightElem = mat[maxiIndex][mid+1] if mid < n-1 else -1
            leftElem = mat[maxiIndex][mid-1] if mid > 0 else -1
            if maxi > rightElem and maxi > leftElem:
                return [maxiIndex, mid]
            if rightElem > maxi:
                return BS(mid+1, high)
            if leftElem > maxi:
                return BS(low, mid-1)
        
        return BS(0, n-1)
            

