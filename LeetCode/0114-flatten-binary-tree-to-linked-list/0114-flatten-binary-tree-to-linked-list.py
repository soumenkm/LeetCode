# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = deque()
        def preorder(node: TreeNode) -> None:
            if node is None:
                return    
            pre.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        def func() -> TreeNode:
            if len(pre) == 0:
                return None
            root = pre.popleft()
            root.left = None
            root.right = func()
            return root
        
        root = func()