class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for i in range(m)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def findAdj(i: int, j: int) -> List[Tuple[int, int]]:
            nonlocal m
            nonlocal n
            adj = []
            for ni, nj in dirs:
                adjRow, adjCol = ni + i, nj + j
                if 0 <= adjRow <= m-1 and 0 <= adjCol <= n-1 and grid[adjRow][adjCol] == "1":
                    adj.append((adjRow, adjCol))
            return adj
 
        def BFS(row: int, col: int) -> None:
            Q = deque()
            Q.append((row, col))
            visited[row][col] = 1

            while len(Q) != 0:
                size = len(Q)
                for i in range(size):
                    nodeRow, nodeCol = Q.popleft()
                    for adjRow, adjCol in findAdj(nodeRow, nodeCol):
                        if visited[adjRow][adjCol] == 0:
                            visited[adjRow][adjCol] = 1
                            Q.append((adjRow, adjCol))
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    BFS(i, j)
                    count += 1
        
        return count