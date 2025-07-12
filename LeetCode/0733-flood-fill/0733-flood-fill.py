class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        res = image.copy()
        
        def find_adj(i: int, j: int) -> List[Tuple[int, int]]:
            adj = []
            for dr, dc in dirs:
                ni = dr + i
                nj = dc + j
                if 0 <= ni < m and 0 <= nj < n and image[ni][nj] == image[sr][sc]:
                    adj.append((ni, nj))
            return adj

        def DFS(i: int, j: int):
            visited[i][j] = 1
            for x, y in find_adj(i, j):
                if visited[x][y] == 0:
                    DFS(x, y)
            res[i][j] = color
        
        DFS(sr, sc)
        return res
        