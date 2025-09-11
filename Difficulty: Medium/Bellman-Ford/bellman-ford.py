#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float("inf") for i in range(V)]
        dist[src] = 0
        
        def relax(dist_u: int, v: int, w: int) -> bool:
            if dist_u + w < dist[v]:
                dist[v] = dist_u + w
                return True
            else:
                return False
        
        for _ in range(V-1):
            tempDist = dist.copy()
            for  u, v, w in edges:
                relax(tempDist[u], v, w)
        
        tempDist = dist.copy()
        for u, v, w in edges:
            if relax(tempDist[u], v, w):
                return [-1]
        
        dist = [10**8 if d == float("inf") else d for d in dist]
        return dist
        
        
            