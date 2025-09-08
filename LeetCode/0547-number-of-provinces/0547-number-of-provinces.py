class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        color = [0 for i in range(n)]
        def DFS(node: int) -> None:
            color[node] = 1
            for adj in adjList[node]:
                if color[adj] == 0:
                    DFS(adj)
        
        count = 0
        for i in range(n):
            if color[i] == 0:
                DFS(i)
                count += 1
        
        return count
