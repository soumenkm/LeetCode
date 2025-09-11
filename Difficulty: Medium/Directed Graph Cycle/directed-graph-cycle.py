
class Solution:
    def isCycle(self, V, edges):
        
        adjList = [[] for i in range(V)]
        for i, j in edges:
            adjList[i].append(j)
        
        color = [0 for i in range(V)]
        def DFS(node: int) -> bool:
            color[node] = 1
            res = False
            for adj in adjList[node]:
                if color[adj] == 0:
                    cycle = DFS(adj)
                elif color[adj] == 1:
                    cycle = True
                else:
                    cycle = False
                res = res or cycle
            color[node] = 2
            return res
        
        res = False
        for i in range(V):
            if color[i] == 0:
                res = res or DFS(i)
        return res