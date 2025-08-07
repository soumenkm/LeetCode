# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def preorder(root: TreeNode) -> List[int]:
        #     if root is None:
        #         return []
            
        #     left = preorder(root.left)
        #     right = preorder(root.right)
        #     res = [root.val]
        #     if left:
        #         res += left
        #     if right:
        #         res += right
        #     return res
        
        res = []
        def preorder(root: TreeNode):
            if root is None:
                return      
            res.append(root.val) 
            left = preorder(root.left)
            right = preorder(root.right)

        preorder(root)
        return res