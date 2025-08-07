# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def func(node: TreeNode) -> Tuple[int, bool]:
            if node is None:
                return [0, True]
            
            leftDepth, leftRes = func(node.left)
            rightDepth, rightRes = func(node.right)
            nodeDepth = max(leftDepth, rightDepth) + 1
            if abs(leftDepth - rightDepth) > 1:
                return [nodeDepth, False]
            elif not leftRes or not rightRes:
                return [nodeDepth, False]
            else:
                return [nodeDepth, True]
        
        _, res = func(root)
        return res