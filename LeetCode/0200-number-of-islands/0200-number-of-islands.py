class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find_adjacent(node: Tuple[int, int]) -> List[Tuple[int, int]]:
            i = node[0]
            j = node[1]
            adj = []
            for dr, dc in dirs:
                ni = dr + i
                nj = dc + j    
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    adj.append((ni, nj))
            return adj

        def DFS(node: Tuple[int, int]):
            visited[node[0]][node[1]] = 1
            for i, j in find_adjacent(node):
                if visited[i][j] == 0:
                    DFS((i, j))
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    DFS((i, j))
                    count += 1
        return count