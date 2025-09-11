from collections import deque
class Solution:
	def isCycle(self, V, edges):
		
		adjList = [[] for i in range(V)]
		for i, j in edges:
		    adjList[i].append(j)
		    adjList[j].append(i)
		
		color = [0 for i in range(V)]
# 		def DFS(node: int, parent: int) -> bool:
# 		    color[node] = 1
# 		    res = False
# 		    for adj in adjList[node]:
# 		        if color[adj] == 0:
# 		            cycle = DFS(adj, node)
# 		        elif color[adj] == 1 and adj != parent:
# 		            cycle = True
# 		        else:
# 		            cycle = False
# 		        res = res or cycle
# 		    color[node] = 2
# 		    return res

        def BFS(start: int) -> bool:
            Q = deque()
            Q.append((start, -1))
            color[start] = 1
            while len(Q) != 0:
                size = len(Q)
                for _ in range(size):
                    node, par = Q.popleft()
                    for adj in adjList[node]:
                        if color[adj] == 1 and adj != par:
                            return True
                        elif color[adj] == 0:
                            color[adj] = 1
                            Q.append((adj, node))
            return False
		
		res = False
		for i in range(V):
		    if color[i] == 0:
		      #  res = res or DFS(i, -1)
		      res = res or BFS(i)
	    return res