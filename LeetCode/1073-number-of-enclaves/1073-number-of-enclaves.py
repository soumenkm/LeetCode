class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def find_adj(i: int, j: int) -> List[Tuple[int, int]]:
            adj = []
            for dr, dc in dirs:
                ni = dr + i
                nj = dc + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    adj.append((ni, nj))   
            return adj 
        
        def DFS(i: int, j: int) -> Tuple[bool, int]:
            visited[i][j] = 1
            is_on_boundary = False
            count = 1
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                is_on_boundary = True
            for x, y in find_adj(i, j):
                if visited[x][y] == 0:
                    res, adj_count = DFS(x, y)
                    count = count + adj_count
                    if res:
                        is_on_boundary = True
            return is_on_boundary, count

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    res, ind_count = DFS(i, j)
                    if not res:
                        count = count + ind_count
        return count