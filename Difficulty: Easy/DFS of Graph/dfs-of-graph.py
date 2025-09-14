class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        n = len(adj)
        color = [0 for i in range(n)]
        res = []
        def DFS(node: int):
            color[node] = 1
            res.append(node)
            for adjNode in adj[node]:
                if color[adjNode] == 0:
                    DFS(adjNode)
        
        for i in range(n):
            if color[i] == 0:
                DFS(i)
        
        return res