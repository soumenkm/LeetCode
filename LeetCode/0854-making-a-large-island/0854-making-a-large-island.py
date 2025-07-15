class DisjointSet:
    def __init__(self, ones: List[Tuple[int, int]]):
        self.n = len(ones)
        self.size = {i: 1 for i in ones}
        self.parent = {i: i for i in ones}
    
    def find(self, node: Tuple[int, int]) -> Tuple[int, int]:
        par = self.parent[node]
        if par == node:
            return node
        else:
            res = self.find(par)
            self.parent[node] = res
            return res
    
    def union(self, node1:Tuple[int, int], node2: Tuple[int, int]):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 != node2:
            if self.size[node1] >= self.size[node2]:
                self.parent[node2] = node1
                self.size[node1] += self.size[node2]
            else:
                self.parent[node1] = node2
                self.size[node2] += self.size[node1]
    
    def get_comps(self) -> Dict[Tuple[int, int], int]:
        roots = defaultdict(int)
        for node in self.parent:
            upar = self.find(node)
            roots[upar] += 1
        return roots

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        zeros = []
        ones = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                else:
                    ones.append((i, j))
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def find_adj(node: Tuple[int, int]) -> List[Tuple[int, int]]:
            adj = []
            i, j = node
            for r, c in dirs:
                ni = i + r
                nj = j + c
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    adj.append((ni, nj))
            return adj

        dset = DisjointSet(ones)
        for node in ones:
            for adj in find_adj(node):
                if dset.find(node) != dset.find(adj):
                    dset.union(node, adj)
        comps = dset.get_comps()

        size = {i: 1 for i in zeros}
        for node in zeros:
            roots = set()
            for adj in find_adj(node):
                roots.add(dset.find(adj))
            for r in roots:
                size[node] += comps[r]
                
        return max(size.values()) if size else m * n