# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pre_p = []
        in_p = []
        pre_q = []
        in_q = []
        def func(root: TreeNode, node: str):
            if root is None and node == "p":
                pre_p.append("NULL")
                in_p.append("NULL")
                return
            
            if root is None and node == "q":
                pre_q.append("NULL")
                in_q.append("NULL")
                return

            if node == "p":
                pre_p.append(root.val)
                func(root.left, node)
                in_p.append(root.val)
                func(root.right, node)
            
            if node == "q":
                pre_q.append(root.val)
                func(root.left, node)
                in_q.append(root.val)
                func(root.right, node)

        func(p, "p")
        func(q, "q")

        if pre_p == pre_q and in_p == in_q:
            return True
        else:
            return False