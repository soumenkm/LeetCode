class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        adj_list = {}
        dirs = [(0,-1), (0,1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    adj_list[(i,j)] = []
                    for dr, dc in dirs:
                        ni = i + dr
                        nj = j + dc
                        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O":
                            adj_list[(i,j)].append((ni,nj))
                            
        V = len(adj_list)
        boundary_nodes = []
        for i, j in adj_list.keys():
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                boundary_nodes.append((i,j))
        
        color = {(i,j): 0 for i,j in adj_list.keys()}
        def DFS(node: Tuple[int, int]):
            color[node] = 1
            for adj in adj_list[node]:
                if color[adj] == 0:
                    DFS(adj)
            color[node] = 2
        
        for i, j in boundary_nodes:
            if color[(i,j)] == 0:
                DFS((i,j))

        for i,j in adj_list.keys():
            if color[(i,j)] == 0:
                board[i][j] = "X"
        


        