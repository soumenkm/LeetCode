# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        preorder = [TreeNode(p) for p in preorder]
        n = len(preorder)
        pre = 1
        def func(root: TreeNode, lb: int, ub: int) -> TreeNode:
            nonlocal pre
            if pre == n:
                root.left = None
                root.right = None
                return root

            if lb < preorder[pre].val < root.val:
                pre = pre + 1
                root.left = func(preorder[pre-1], lb, root.val)
            else:
                root.left = None
            
            if pre == n:
                return root

            if root.val < preorder[pre].val < ub:
                pre = pre + 1
                root.right = func(preorder[pre-1], root.val, ub)
            else:
                root.right = None
            
            return root

        root = func(preorder[0], -math.inf, math.inf)
        return root