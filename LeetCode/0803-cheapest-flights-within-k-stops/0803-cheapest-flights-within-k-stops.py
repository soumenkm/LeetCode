class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for i in range(n)]
        for u, v, w in flights:
            adjList[u].append((v, w))

        dist = [math.inf for u in range(n)]
        dist[src] = 0
        Q = deque([(0, src, 0)])

        while len(Q) != 0:
            s, node, d = Q.popleft()
            for adj, w in adjList[node]:
                if d + w < dist[adj] and s <= k:
                    dist[adj] = d + w
                    Q.append((s+1, adj, dist[adj]))
        if dist[dst] == math.inf:
            return -1
        else:
            return dist[dst]