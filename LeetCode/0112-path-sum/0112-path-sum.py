# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def func(node: TreeNode, currSum: int) -> bool:
            if node.left is None and node.right is None:
                return currSum == targetSum

            if node.left is not None and func(node.left, currSum + node.left.val):
                return True
            if node.right is not None and func(node.right, currSum + node.right.val):
                return True
            return False
        
        return func(root, root.val)
