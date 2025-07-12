class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adjList[u].append((v, w))
        INF = math.inf
        dist = {i: INF for i in adjList}
        dist[k] = 0
        PQ = []
        heapq.heappush(PQ, (0, k))
   
        while len(PQ) != 0:
            d, node = heapq.heappop(PQ)
            for adj, w in adjList[node]:
                if d + w < dist[adj]:
                    dist[adj] = d + w
                    heapq.heappush(PQ, (d+w, adj))
    
        maxDist = max(dist.values())
        return maxDist if maxDist < INF else -1