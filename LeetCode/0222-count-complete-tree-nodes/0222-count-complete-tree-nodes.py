# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def func(node: TreeNode) -> int:
            if node is None:
                return 0
            
            temp = copy.deepcopy(node)
            leftHeight = 0
            while temp is not None:
                temp = temp.left
                leftHeight += 1
            
            temp = copy.deepcopy(node)
            rightHeight = 0
            while temp is not None:
                temp = temp.right
                rightHeight += 1

            if leftHeight == rightHeight:
                return 2**leftHeight - 1

            leftCount = func(node.left)
            rightCount = func(node.right)
            return 1 + leftCount + rightCount
        
        return func(root)