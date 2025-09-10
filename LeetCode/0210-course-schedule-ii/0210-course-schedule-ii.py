class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adjList = [[] for i in range(n)]
        indeg = [0 for i in range(n)]
        for a, b in prerequisites:
            adjList[b].append(a)
            indeg[a] += 1
        
        Q = deque()
        for i in range(n):
            if indeg[i] == 0:
                Q.append(i)
        
        topo = []
        while len(Q) != 0:
            size = len(Q)
            for _ in range(size):
                node = Q.popleft()
                topo.append(node)
                for adj in adjList[node]:
                    if indeg[adj] == 1:
                        indeg[adj] = 0
                        Q.append(adj)
                    elif indeg[adj] > 1:
                        indeg[adj] -= 1

        if len(topo) != n:
            return []
        else:
            return topo