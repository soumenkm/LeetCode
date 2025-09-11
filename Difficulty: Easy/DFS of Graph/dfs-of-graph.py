class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        res = []
        n = len(adj)
        start = [0] * n
        finish = [0] * n
        color = [0] * n
        time = 0
        
        def DFS(node: int) -> None:
            nonlocal time
            color[node] = 1
            time += 1
            start[node] = time
            res.append(node)
            
            for adjacent in adj[node]:
                if color[adjacent] == 0:
                    DFS(adjacent)
            
            time += 1
            finish[node] = time
            color[node] = 2
        
        DFS(0)
        return res