# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        Q = deque()
        Q.append(root)
        level = 0
        res = []
        while len(Q) != 0:
            n = len(Q)
            intRes = None
            for i in range(n):
                node = Q.popleft()
                if node.left is not None:
                    Q.append(node.left)
                if node.right is not None:
                    Q.append(node.right)
                intRes = node.val
            res.append(intRes)
            level = level + 1
    
        return res