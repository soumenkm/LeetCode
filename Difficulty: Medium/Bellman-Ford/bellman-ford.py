#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float("inf") for i in range(V)]
        dist[src] = 0
        
        def relax(u: int, v: int, w: int) -> bool:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                return True
            else:
                return False
        
        for _ in range(V-1):
            for  u, v, w in edges:
                relax(u, v, w)
        
        for u, v, w in edges:
            if relax(u, v, w):
                return [-1]
        
        dist = [10**8 if d == float("inf") else d for d in dist]
        return dist
        
        
            