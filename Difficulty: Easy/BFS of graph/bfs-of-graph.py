from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n = len(adj)
        res = []
        color = [0 for i in range(n)]
        
        def BFS(src: int):
            Q = deque()
            Q.append(src)
            color[src] = 1
            
            while len(Q) != 0:
                size = len(Q)
                for _ in range(size):
                    node = Q.popleft()
                    res.append(node)
                    for adjNode in adj[node]:
                        if color[adjNode] == 0:
                            color[adjNode] = 1
                            Q.append(adjNode)
        
        for i in range(n):
            if color[i] == 0:
                BFS(i)
        
        return res
        