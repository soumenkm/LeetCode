# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        n = v
        adjList = [[] for i in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        color = [-1 for i in range(n)]
        
        def isSafe(node: int, c: int) -> bool:
            for adj in adjList[node]:
                if color[adj] == c:
                    return False
            return True
            
        def DFS(node: int) -> bool:
            for c in range(m):
                if isSafe(node, c):
                    color[node] = c
                    res = True
                    for adj in adjList[node]:
                        if color[adj] == -1:
                            intRes = DFS(adj)
                            res = res and intRes
                            if not res:
                                break
                    if res:
                        return res
            return False
        
        for node in range(n):
            if color[node] == -1:
                intRes = DFS(node)
                if not intRes:
                    return False
        
        return True
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                    
                    