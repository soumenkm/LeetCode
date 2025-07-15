class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, u: int) -> int:
        pu = self.parent[u]
        if pu == u:
            return u
        else:
            upu = self.find(pu)
            self.parent[u] = upu
            return upu
    
    def union(self, u: int, v: int):
        u = self.parent[u]
        v = self.parent[v]
        if u != v:
            if self.size[u] >= self.size[v]:
                self.parent[v] = u
                self.size[u] += self.size[v]
            elif self.size[u] < self.size[v]:
                self.parent[u] = v
                self.size[v] += self.size[u]
    
    def num_comp(self) -> int:
        count = 0
        for i in range(self.n):
            if i == self.parent[i]:
                count += 1
        return count

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        A = []
        for u, v in connections:
            if ds.find(u) == ds.find(v):
                A.append((u, v))
            else:
                ds.union(u, v)
        
        k = ds.num_comp()
        if len(A) >= k - 1:
            return  k - 1
        else:
            return -1