# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def func(node: TreeNode, isLeft: bool) -> int:
            if node.left is None and node.right is None:
                if isLeft:
                    return node.val
                else:
                    return 0
            if node.left is not None:
                left = func(node.left, True)
            else:
                left = 0
            if node.right is not None:
                right = func(node.right, False)
            else:
                right = 0
            return left + right
        
        return func(root, False)