class DisjointSet:
    def __init__(self, nodes: List[Tuple[int, int]]):
        self.n = nodes
        self.s = {tuple(i): 1 for i in nodes}
        self.p = {tuple(i): tuple(i) for i in nodes}
    
    def find(self, node: Tuple[int, int]) -> Tuple[int, int]:
        par = self.p[node]
        if par == node:
            return node
        else:
            res = self.find(par)
            self.p[node] = res
            return res
    
    def union(self, node1: Tuple[int, int], node2: Tuple[int, int]):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 != node2:
            if self.s[node1] >= self.s[node2]:
                self.p[node2] = node1
                self.s[node1] += self.s[node2]
            else:
                self.p[node1] = node2
                self.s[node2] += self.s[node1]

    def num_comps(self) -> int:
        count = 0
        for node, par in self.p.items():
            if node == par:
                count += 1
        return count

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        for x, y in stones:
            rowMap[x].append((x, y))
            colMap[y].append((x, y))
        
        edges = set()
        for x, y in stones:
            for u, v in rowMap[x]:
                if (u, v) != (x, y):
                    if ((x, y), (u, v)) not in edges and ((u, v), (x, y)) not in edges:
                        edges.add(((x, y), (u, v)))
            for u, v in colMap[y]:
                if (u, v) != (x, y):
                    if ((x, y), (u, v)) not in edges and ((u, v), (x, y)) not in edges:
                        edges.add(((x, y), (u, v)))
        
        dset = DisjointSet(stones)
        for node1, node2 in edges:
            if dset.find(node1) != dset.find(node2):
                dset.union(node1, node2)
        
        res = n - dset.num_comps()
        return res