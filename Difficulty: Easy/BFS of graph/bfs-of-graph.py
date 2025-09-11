from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n = len(adj)
        color = [0 for i in range(n)]
        
        Q = deque()
        Q.append(0)
        color[0] = 1
        res = []
        
        while len(Q) != 0:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                res.append(node)
                
                for adjNode in adj[node]:
                    if color[adjNode] == 0:
                        color[adjNode] = 1
                        Q.append(adjNode)
        
        return res
        