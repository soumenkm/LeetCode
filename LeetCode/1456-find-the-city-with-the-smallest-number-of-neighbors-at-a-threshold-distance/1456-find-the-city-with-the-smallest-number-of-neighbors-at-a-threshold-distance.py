class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf for j in range(n)] for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        adjMatrix = [[0 for j in range(n)] for i in range(n)]
        for u, v, w in edges:
            dist[u][v] = w if u != v else 0
            dist[v][u] = w if u != v else 0
            adjMatrix[u][v] = 1 if u != v else 0
            adjMatrix[v][u] = 1 if u != v else 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        count = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count[i] += 1
        
        minCount = min(count)
        res = []
        for i in range(n):
            if count[i] == minCount:
                res.append(i)
        return max(res)
        
