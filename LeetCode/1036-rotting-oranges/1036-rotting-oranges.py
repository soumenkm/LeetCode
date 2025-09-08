class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     num_fresh = 0
    #     rot = []
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 num_fresh += 1
    #             if grid[i][j] == 2:
    #                 rot.append((i, j))
        
    #     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     def find_adj(i: int, j: int) -> List[int]:
    #         res = []
    #         for r, c in dirs:
    #             ni = r + i
    #             nj = c + j
    #             if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
    #                 res.append((ni, nj))
    #         return res

    #     visited = [[0 for j in range(n)] for i in range(m)]
    #     time = 0
    #     Q = deque([(i, j, time) for i, j in rot])
    #     for i, j in rot:
    #         visited[i][j] = 1

    #     while len(Q) != 0:
    #         i, j, time = Q.popleft()
    #         adj = find_adj(i, j)
    #         for ni, nj in adj:
    #             if visited[ni][nj] == 0:
    #                 Q.append((ni, nj, time+1))
    #                 visited[ni][nj] = 1
        
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1 and visited[i][j] == 0:
    #                 return -1
    #     return time


    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = []
        freshCount = 0
        visited = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        
        if freshCount == 0:
            return 0

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def findAdj(i: int, j: int) -> List[Tuple[int, int]]:
            res = []
            for r, c in dirs:
                ni = r + i
                nj = c + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    res.append((ni, nj))
            return res

        Q = deque()
        for i, j in rotten:
            Q.append((i, j))
            visited[i][j] = 1
        
        count = 0
        mint = 0
        while len(Q) != 0:
            size = len(Q)
            mint += 1
            for _ in range(size):
                i, j = Q.popleft()
                for ni, nj in findAdj(i, j):
                    if visited[ni][nj] == 0:
                        count += 1
                        visited[ni][nj] = 1
                        Q.append((ni, nj))

        if freshCount == count:
            return mint-1
        else:
            return -1



                

        