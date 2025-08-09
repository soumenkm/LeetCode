# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        def func(node: TreeNode, val: int, parent: TreeNode):
            if node is None:
                if val < parent.val:
                    parent.left = TreeNode(val) 
                else:
                    parent.right = TreeNode(val)
                return
            if val < node.val:
                func(node.left, val, node)
            else:
                func(node.right, val, node)

        func(root, val, None)
        return root