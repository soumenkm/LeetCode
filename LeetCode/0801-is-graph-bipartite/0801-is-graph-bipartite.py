class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]
        visited = [0 for i in range(len(graph))]

        def DFS(node: int, c: int):
            visited[node] = 1
            color[node] = c
            is_bipar = True
            for adj in graph[node]:
                if visited[adj] == 0:
                    res = DFS(adj, 1) if c == 0 else DFS(adj, 0)
                    if not res:
                        is_bipar = False
                else:
                    if color[node] == color[adj]:
                        is_bipar = False
            return is_bipar
        
        res = True
        for i in range(len(graph)):
            if visited[i] == 0:
                res = res and DFS(i, 0)
            if not res:
                break
        return res