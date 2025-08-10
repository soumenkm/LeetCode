# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def inorder(node: TreeNode) -> int:
            nonlocal count
            if node is None:
                return None
            
            res1 = inorder(node.left)
            count = count + 1
            if count == k:
                return node.val
            res2 = inorder(node.right)
            
            if res1 is None and res2 is None:
                return None
            if res1 is None and res2 is not None:
                return res2
            if res1 is not None and res2 is None:
                return res1

        res = inorder(root)
        return res