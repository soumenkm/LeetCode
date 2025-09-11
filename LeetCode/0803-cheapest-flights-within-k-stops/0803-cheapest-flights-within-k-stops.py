class Solution:
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf for i in range(n)]
        dist[src] = 0

        def relax(tempDist: List[int], u: int, v: int, w: int):
            if tempDist[u] + w < dist[v]:
                dist[v] = tempDist[u] + w
        
        for _ in range(k+1):
            tempDist = dist.copy()
            for u, v, w in flights:
                relax(tempDist, u, v, w)
        
        return dist[dst] if dist[dst] != math.inf else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for i in range(n)]
        for u, v, w in flights:
            adjList[u].append((v, w))

        dist = [math.inf for i in range(n)]
        dist[src] = 0

        def relax(dist_u: int, v: int, w: int, stops: int) -> bool:
            if dist_u + w < dist[v] and stops < k+1:
                dist[v] = dist_u + w
                return True
            else:
                return False
        
        Q = deque()
        Q.append((0, src, 0))
        while len(Q) != 0:
            stops, node, d = Q.popleft()
            for adj, w in adjList[node]:
                if relax(d, adj, w, stops):
                    Q.append((stops+1, adj, dist[adj]))
        
        return dist[dst] if dist[dst] != math.inf else -1

            