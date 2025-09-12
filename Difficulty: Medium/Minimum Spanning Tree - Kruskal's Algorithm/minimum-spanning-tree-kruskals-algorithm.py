#User function Template for python3
from typing import List

class DisjointSet:
    def __init__(self, n: int) -> None:
        self.n = n
        self.size = [1 for i in range(self.n)]
        self.par = [i for i in range(self.n)]
    
    def find(self, u: int) -> int:
        if self.par[u] == u:
            return u
        else:
            root = self.find(self.par[u])
            self.par[u] = root
            return root
            
    def union(self, u: int, v:int):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return 
        
        if self.size[u] >= self.size[v]:
            self.par[v] = u
            self.size[u] += self.size[v]
        else:
            self.par[u] = v
            self.size[v] += self.size[u]

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        edges = sorted(edges, key=lambda elem: elem[-1])
        dset = DisjointSet(V)
        weight = 0
        for u, v, w in edges:
            if dset.find(u) != dset.find(v):
                dset.union(u, v)
                weight += w
        return weight
        
        