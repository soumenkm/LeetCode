class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        color = [0 for i in range(V)]
        safe = [None for i in range(V)]
        
        def DFS(node: int):
            color[node] = 1
            is_safe = True
            for adj in graph[node]:
                if color[adj] == 0:
                    DFS(adj)
                    is_safe = (is_safe and safe[adj])
                elif color[adj] == 1:
                    is_safe = False
                elif color[adj] == 2 and safe[adj] == False:
                    is_safe = False
            color[node] = 2
            safe[node] = is_safe
            
        for i in range(V):
            if color[i] == 0:
                DFS(i)
        safe_map = list(zip(range(V), safe))
        res = sorted(list(filter(lambda x: x[1] == True, safe_map)))
        return [i for i, _ in res]