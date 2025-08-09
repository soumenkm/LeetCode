# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def func(node: TreeNode, val: int) -> TreeNode:
            if node is None:
                return None
            if val == node.val:
                return node
            elif val < node.val:
                return func(node.left, val)
            elif val > node.val:
                return func(node.right, val)
        
        return func(root, val)