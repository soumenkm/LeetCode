class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        V = numCourses
        adj_list = [[] for i in range(V)]
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        color = [0 for i in range(V)]
        def DFS(node: int) -> bool:
            color[node] = 1
            has_cycle = False
            for adj in adj_list[node]:
                if color[adj] == 0:
                    res = DFS(adj)
                    has_cycle = (has_cycle or res)
                elif color[adj] == 1:
                    has_cycle = True
            color[node] = 2
            return has_cycle
        
        has_cycle = False
        for i in range(V):
            if color[i] == 0:
                res = DFS(i)
                has_cycle = (has_cycle or res)
        return not has_cycle