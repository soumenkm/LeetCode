class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m = len(grid)
        n = len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        def find_adj(node: Tuple[int, int]) -> List[Tuple[int, int]]:
            adj = []
            i, j = node
            for r, c in dirs:
                ni = i + r
                nj = j + c
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    adj.append((ni, nj))
            return adj

        dist = [[math.inf for j in range(n)] for i in range(m)]
        dist[0][0] = 1
        Q = []
        heapq.heappush(Q, (1, (0, 0)))

        while len(Q) != 0:
            d, node = heapq.heappop(Q)
            for adj in find_adj(node):
                current_d = d + 1
                if current_d < dist[adj[0]][adj[1]]:
                    dist[adj[0]][adj[1]] = current_d
                    heapq.heappush(Q, (current_d, adj))
        
        if dist[m-1][n-1] == math.inf:
            return -1
        else:
            return dist[m-1][n-1]

     