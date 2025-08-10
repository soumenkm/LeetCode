# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        currentMax = -math.inf
        def inorder(node: TreeNode) -> bool:
            nonlocal currentMax
            if node is None:
                return True
            
            res1 = inorder(node.left)
            if not res1:
                return False

            if node.val > currentMax:
                currentMax = node.val
            else:
                return False
            
            res2 = inorder(node.right)
            if not res2:
                return False
            
            return True
        
        return inorder(root)