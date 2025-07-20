class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(n)]
        for a, b in paths:
            adjList[a-1].append(b-1)
            adjList[b-1].append(a-1)
        
        visited = [0 for i in range(n)]
        color = [0 for i in range(n)]

        def isSafe(node: int, c: int):
            for adj in adjList[node]:
                if color[adj] == c:
                    return False
            return True

        def DFS(node: int):
            visited[node] = 1
            for c in range(1, 5):
                if isSafe(node, c):
                    color[node] = c
                    for adj in adjList[node]:
                        if visited[adj] == 0:
                            DFS(adj)
                    return
                else:
                    continue
        
        for i in range(n):
            if visited[i] == 0:
                DFS(i)

        return color
        