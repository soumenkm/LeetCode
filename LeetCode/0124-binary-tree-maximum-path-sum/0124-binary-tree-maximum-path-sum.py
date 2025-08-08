# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currSum = -math.inf
        def func(node: TreeNode) -> int:
            nonlocal currSum
            if node is None:
                return 0
            
            leftLeafSum = max(0, func(node.left))
            rightLeafSum = max(0, func(node.right))
            nodeLeafSum = node.val + max(leftLeafSum, rightLeafSum)
            currSum = max(currSum, node.val + leftLeafSum + rightLeafSum)
            return nodeLeafSum

        func(root)
        return currSum