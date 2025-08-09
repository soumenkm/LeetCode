# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
        
        visited = {i: 0 for i in adjList}
        Q = deque()
        Q.append(target.val)
        visited[target.val] = 1
        level = 0
        res = []
        while len(Q) != 0:
            n = len(Q)
            intRes = []
            for i in range(n):
                elem = Q.popleft()
                intRes.append(elem)
                for adj in adjList[elem]:
                    if visited[adj] == 0:
                        visited[adj] = 1
                        Q.append(adj)
            res.append(intRes)
            level += 1
            if level == k+1:
                return intRes
        
        return []