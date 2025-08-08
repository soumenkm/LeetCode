# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque()
        Q.append(root)
        res = []
        level = 0
        while len(Q) != 0:
            n = len(Q)
            intRes = [] 
            for i in range(n):
                node = Q.popleft()
                intRes.append(node.val)
                if node.left is not None:
                    Q.append(node.left)
                if node.right is not None:
                    Q.append(node.right)
            if level % 2 == 0:
                res.append(intRes)
            else:
                res.append(intRes[::-1])
            level = level + 1
        
        return res