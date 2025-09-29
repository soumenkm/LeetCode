# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        def func(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return 1
            elif node.left is None and node.right is not None:
                return func(node.right) + 1
            elif node.left is not None and node.right is None:
                return func(node.left) + 1
            elif node.left is not None and node.right is not None:
                return min(func(node.left), func(node.right)) + 1
        
        return func(root)