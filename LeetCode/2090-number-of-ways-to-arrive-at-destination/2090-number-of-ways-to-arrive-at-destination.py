class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        src = 0
        dest = n - 1
        adjList = [[] for i in range(n)]
        for u, v, w in roads:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        dist = [math.inf for i in range(n)]
        ways = [0 for i in range(n)]
        PQ = []
        heapq.heappush(PQ, (0, src))
        dist[src] = 0
        ways[src] = 1

        while len(PQ) != 0:
            d, node = heapq.heappop(PQ)
            for adj, w in adjList[node]:
                if d + w < dist[adj]:
                    dist[adj] = d + w
                    heapq.heappush(PQ, (d+w, adj))
                    ways[adj] = ways[node]
                elif d + w == dist[adj]:
                    ways[adj] += ways[node]
        MOD = 10**9 + 7
        return ways[-1] % MOD