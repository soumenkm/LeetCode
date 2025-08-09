# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjList = defaultdict(list)
        Q = deque()
        Q.append(root)
        while len(Q) != 0:
            n = len(Q)
            for i in range(n):
                node = Q.popleft()
                if node.left is not None:
                    Q.append(node.left)
                    adjList[node.val].append(node.left.val)
                    adjList[node.left.val].append(node.val)
                if node.right is not None:
                    Q.append(node.right)
                    adjList[node.val].append(node.right.val)
                    adjList[node.right.val].append(node.val)
        
        Q = deque()
        Q.append(start)
        visited = {i: 0 for i in adjList}
        visited[start] = 1
        level = 0
        while len(Q) != 0:
            n = len(Q)
            for i in range(n):
                node = Q.popleft()
                for adj in adjList[node]:
                    if visited[adj] == 0:
                        visited[adj] = 1
                        Q.append(adj)
            level += 1
        
        return level-1