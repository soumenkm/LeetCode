class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adjList = [[] for i in range(n)]
        for a, b in prerequisites:
            adjList[b].append(a)
        
        color = [0 for i in range(n)]
        def DFS(node: int) -> bool:
            color[node] = 1
            for adj in adjList[node]:
                if color[adj] == 1:
                    return False
                if color[adj] == 0:
                    if not DFS(adj):
                        return False
            color[node] = 2
            return True
        
        for i in range(n):
            if color[i] == 0:
                if not DFS(i):
                    return False
        return True