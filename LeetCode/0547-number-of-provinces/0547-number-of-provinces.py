class Graph:
    def __init__(self, adj_matrix: List[List[int]]):
        self.matrix = adj_matrix
        self.V = len(self.matrix)
        self.list = self._get_adj_list()
        self.color = [0 for i in range(self.V)]
        self.dfs_order = []
        
    def _get_adj_list(self) -> List[List[int]]:
        adj_list = [[] for i in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                if self.matrix[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        return adj_list
    
    def DFS(self, node: int) -> List[int]: 
        self.color[node] = 1 # Mark gray
        self.dfs_order.append(node)
        for adj in self.list[node]:
            if self.color[adj] == 0:
                self.DFS(adj) # If white then call
        self.color[node] = 2 # Mark black

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = Graph(isConnected)
        count = 0
        for i in range(graph.V):
            if graph.color[i] == 0:
                graph.DFS(i)
                count = count + 1
        return count