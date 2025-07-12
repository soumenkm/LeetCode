class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        grid_set = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem != ".":
                    if elem in row_set[i]:
                        return False
                    else:
                        row_set[i].add(elem)
                    if elem in col_set[j]:
                        return False
                    else:
                        col_set[j].add(elem)
                    if elem in grid_set[i//3][j//3]:
                        return False
                    else:
                        grid_set[i//3][j//3].add(elem)
        return True
            