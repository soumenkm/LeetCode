class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i: set() for i in range(9)}
        colMap = {i: set() for i in range(9)}
        blockMap = {(i, j): set() for i in range(3) for j in range(3)}
        
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem != ".":
                    if elem not in rowMap[i]:
                        rowMap[i].add(elem)
                    else:
                        return False
                    if elem not in colMap[j]:
                        colMap[j].add(elem)
                    else:
                        return False
                    br = i // 3
                    bc = j // 3
                    if elem not in blockMap[(br, bc)]:
                        blockMap[(br, bc)].add(elem)
                    else:
                        return False
        return True
