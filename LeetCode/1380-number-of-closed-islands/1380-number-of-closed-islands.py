class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range (m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find_adj(i: int, j: int) -> List[Tuple[int, int]]:
            adj = []
            for dr, dc in dirs:
                ni = i + dr
                nj = j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    adj.append((ni, nj))
            return adj

        def DFS(i: int, j: int) -> bool:
            visited[i][j] = 1
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                is_on_border = True
            else:
                is_on_border = False
            for x, y in find_adj(i, j):
                if visited[x][y] == 0:
                    if DFS(x, y):
                        is_on_border = True
            return is_on_border
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] == 0:
                    has_border = DFS(i, j)
                    if not has_border:
                        count += 1
        return count