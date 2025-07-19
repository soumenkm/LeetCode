class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowMap = {i: set() for i in range(9)}
        colMap = {i: set() for i in range(9)}
        blockMap = {(i,j): set() for i in range(3) for j in range(3)}
        empty = []
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem == ".":
                    empty.append((i, j))
                else:
                    rowMap[i].add(elem)
                    colMap[j].add(elem)
                    blockMap[(i//3, j//3)].add(elem)
        
        def isSafe(row: int, col: int, val: int) -> bool:
            if val in rowMap[row]:
                return False
            if val in colMap[col]:
                return False
            if val in blockMap[(row//3, col//3)]:
                return False
            return True

        def func(k: int) -> bool:
            if k == len(empty):
                return True
            r, c = empty[k]
            
            for val in range(1, 10):
                val = str(val)
                if isSafe(r, c, val):
                    board[r][c] = val
                    rowMap[r].add(val)
                    colMap[c].add(val)
                    blockMap[(r//3, c//3)].add(val) 
                    
                    intRes = func(k+1)
                    if intRes:
                        return True
                        
                    board[r][c] = "."
                    rowMap[r].remove(val)
                    colMap[c].remove(val)
                    blockMap[(r//3, c//3)].remove(val)   
               
            return False
        
        func(0)

        