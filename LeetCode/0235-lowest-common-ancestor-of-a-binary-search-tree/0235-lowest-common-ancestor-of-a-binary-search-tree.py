# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            if p.val < node.val and q.val > node.val:
                return node
            if q.val < node.val and p.val > node.val:
                return node
            if p.val < node.val and q.val < node.val:
                res = func(node.left)
            if p.val > node.val and q.val > node.val:
                res = func(node.right)
            return res
        
        return func(root)