# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def func(node: TreeNode) -> int:
            if node is None:
                return 0
            
            left = func(node.left)
            right = func(node.right)
            return max(left, right) + 1
        return func(root)
            