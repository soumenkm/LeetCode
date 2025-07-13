class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        def calc_effort(node1: Tuple[int, int], node2: Tuple[int, int]) -> int:
            i, j = node1
            k, l = node2
            return abs(heights[i][j] - heights[k][l])
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def find_adj(node: Tuple[int]) -> List[Tuple[Tuple[int], int]]:
            # ((ni, nj), max effort))
            adj = []
            i, j = node
            for r, c in dirs:
                ni = r + i
                nj = c + j
                if 0 <= ni < m and 0 <= nj < n:
                    neigh = (ni, nj)
                    maxEffort = calc_effort(node, neigh)
                    adj.append((neigh, maxEffort))
            return adj
        
        min_maxEffort = [[math.inf for j in range(n)] for i in range(m)]
        min_maxEffort[0][0] = 0
        Q = []
        heapq.heappush(Q, (0, (0, 0)))
        
        while len(Q) != 0:
            maxEffort, node = heapq.heappop(Q)
            for adj, w in find_adj(node):
                curr_maxEffort = max(maxEffort, w)
                if curr_maxEffort < min_maxEffort[adj[0]][adj[1]]:
                    min_maxEffort[adj[0]][adj[1]] = curr_maxEffort
                    heapq.heappush(Q, (curr_maxEffort, adj))
        
        return min_maxEffort[m-1][n-1]