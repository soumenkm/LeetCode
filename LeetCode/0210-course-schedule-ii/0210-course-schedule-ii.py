class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        V = numCourses
        adj_list = [[] for i in range(V)]
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        color = [0 for i in range(V)]
        start = [None for i in range(V)]
        finish = [None for i in range(V)]
        time = 0
        
        def DFS(node: int) -> bool:
            nonlocal time
            color[node] = 1
            time = time + 1
            start[node] = time
            has_cycle = False
            
            for adj in adj_list[node]:
                if color[adj] == 0:
                    has_cycle = (has_cycle or DFS(adj))
                elif color[adj] == 1:
                    has_cycle = True

            color[node] = 2
            time = time + 1
            finish[node] = time
            return has_cycle
        
        has_cycle = False
        for i in range(V):
            if color[i] == 0:
                has_cycle = (has_cycle or DFS(i))
        
        if has_cycle:
            return []
        else:
            res = list(zip(finish, range(V))) 
            res = sorted(res, key=lambda x: x[0], reverse=True)
            return [j for i, j in res]