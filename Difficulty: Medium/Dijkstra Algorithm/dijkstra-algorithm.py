import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adjList = [[] for i in range(V)]
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        dist = [float("inf") for i in range(V)]
        par = [None for i in range(V)]
        
        PQ = []
        heapq.heappush(PQ, (0, src))
        dist[src] = 0
        par[src] = -1
        
        def relax(u: int, v: int, w: int) -> bool:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                par[v] = u
                return True
            else:
                return False
        
        while len(PQ) != 0:
            d, u = heapq.heappop(PQ)
            if d > dist[u]:
                continue
            for v, w  in adjList[u]:
                if relax(u, v, w):
                    heapq.heappush(PQ, (dist[v], v))
        
        return dist
            