class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        V = len(edges)
        adj_list = [[] for i in range(V)]
        for i in range(V):
            if edges[i] != -1:
                adj_list[i].append(edges[i])

        color = [0 for i in range(V)]
        depth = [0 for i in range(V)]
        cycle = []

        def DFS(node: int):
            color[node] = 1
            for adj in adj_list[node]:
                if color[adj] == 0:
                    depth[adj] = depth[node] + 1
                    DFS(adj)
                elif color[adj] == 1:
                    count = depth[node] - depth[adj] + 1
                    cycle.append(count)       
            color[node] = 2

        for i in range(V):
            if color[i] == 0:
                DFS(i)
        
        return max(cycle) if cycle else -1