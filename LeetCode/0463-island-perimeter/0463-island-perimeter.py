class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        edge = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def find_adj(node: Tuple[int, int]) -> List[Tuple[int, int]]:
            i = node[0]
            j = node[1]
            adj = []
            for dr, dc in dirs:
                ni = dr + i
                nj = dc + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    adj.append((ni, nj))
            return adj

        def DFS(node: Tuple[int, int]):
            i = node[0]
            j = node[1]
            visited[i][j] = 1
            adj = find_adj(node)
            edge.append(4 - len(adj))
            for x, y in adj:
                if visited[x][y] == 0:
                    DFS((x, y))
        
        island_found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    DFS((i, j))
                    island_found = True
                    break
            if island_found:
                break
        
        perimeter = sum(edge)
        return perimeter
