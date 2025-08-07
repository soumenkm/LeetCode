# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def func(node: TreeNode) -> [int, int]:
            if node is None:
                return [0, 0]
            
            leftDepth, leftDia = func(node.left)
            rightDepth, rightDia = func(node.right)
            nodeDepth = 1 + max(leftDepth, rightDepth)
            nodeDia = max(leftDepth + rightDepth, leftDia, rightDia)
            return nodeDepth, nodeDia
        
        _, res = func(root)
        return res