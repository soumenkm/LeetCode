class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)

        wordMap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                elem = board[i][j]
                wordMap[elem].append((i, j))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def findAdj(i: int, j: int) -> List[Tuple[int, int]]:
            adj = []
            for r, c in dirs:
                ni = i + r
                nj = j + c
                if 0 <= ni < m and 0 <= nj < n:
                    adj.append((ni, nj))
            return adj

        visited = [[0 for i in range(n)] for i in range(m)]
        def DFS(row: int, col: int, w: int) -> bool:
            if w == k-1:
                return True

            visited[row][col] = 1
            for ni, nj in findAdj(row, col):
                if visited[ni][nj] == 0 and word[w+1] == board[ni][nj]:
                    intRes = DFS(ni, nj, w+1)
                    if intRes:
                        return True
            visited[row][col] = 0
            return False
        
        first = word[0]
        for i, j in wordMap[first]:
            if DFS(i, j, 0):
                return True
        
        return False