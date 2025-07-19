class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(top: Dict[int, int], topLeft: Dict[int, int], topRight: Dict[int, int], a: int, b: int) -> bool:
            if top[b] == 1:
                return False
            if topLeft[a+b] == 1:
                return False
            if topRight[n-1+b-a] == 1:
                return False
            return True
                        
        res = []
        def func(row: int, col: int, comb: List[List[str]], top: Dict[int, int], topLeft: Dict[int, int], topRight: Dict[int, int]):
            print(row, col, comb)
            if row == n:
                res.append(["".join(c) for c in comb.copy()])
            else:
                for j in range(n):
                    if isSafe(top, topLeft, topRight, row, j):
                        comb[row][j] = "Q"
                        top[j] = 1
                        topLeft[row+j] = 1
                        topRight[n-1+j-row] = 1
                        func(row+1, j, comb, top, topLeft, topRight)
                        comb[row][j] = "."
                        top[j] = 0
                        topLeft[row+j] = 0
                        topRight[n-1+j-row] = 0

        comb = [["." for i in range(n)] for i in range(n)]
        top = {i: 0 for i in range(n)}
        topLeft = {i: 0 for i in range(2*n-1)}
        topRight = {i: 0 for i in range(2*n-1)}
        func(0, 0, comb, top, topLeft, topRight)
        return res