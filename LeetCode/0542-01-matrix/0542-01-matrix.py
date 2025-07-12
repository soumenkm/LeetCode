class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zeros.append((i, j, 0))

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def find_adj(i: int, j: int) -> List[int]:
            res = []
            for r, c in dirs:
                ni = r + i
                nj = c + j
                if 0 <= ni < m and 0 <= nj < n:
                    res.append((ni, nj))
            return res

        Q = deque(zeros)
        visited = [[1 if mat[i][j] == 0 else 0 for j in range(n)] for i in range(m)]
        dist = [[0 for j in range(n)] for i in range(m)]

        while len(Q) != 0:
            i, j, d = Q.popleft()
            dist[i][j] = d
            for ni, nj in find_adj(i, j):
                if visited[ni][nj] == 0:
                    Q.append((ni, nj, d+1))
                    visited[ni][nj] = 1
        return dist



