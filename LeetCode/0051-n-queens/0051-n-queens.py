class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        dirs = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,1), (1,-1), (-1,-1)]
        def find_attack_pos(i: int, j: int) -> Set[Tuple[int, int]]:
            res = set()
            def func(i, j, d):
                x, y = d
                ni = i + x
                nj = j + y
                if 0 <= ni < n and 0 <= nj < n:
                    res.add((ni, nj))
                    func(ni, nj, d)
            for d in dirs:
                func(i, j, d)
            return res
        
        def isSafe(config: List[List[str]], a: int, b: int) -> bool:
            attackSet = set()
            for i in range(n):
                for j in range(n):
                    if config[i][j] == "Q":
                        attack = find_attack_pos(i, j)
                        attackSet.update(attack)
            if (a, b) in attackSet:
                return False
            else:
                return True 
                        
        res = []
        def func(row: int, col: int, comb: List[List[str]]):
            if row == n:
                res.append(["".join(c) for c in comb.copy()])
            else:
                for j in range(n):
                    if isSafe(comb, row, j):
                        comb[row][j] = "Q"
                        func(row+1, j, comb)
                        comb[row][j] = "."

        comb = [["." for i in range(n)] for i in range(n)]
        func(0, 0, comb)
        return res