# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def func(node: TreeNode, path: List[str]) -> None:
            if node.left is None and node.right is None:
                res.append("->".join(path))
                return
            
            if node.left is not None:
                path.append(str(node.left.val))
                func(node.left, path)
                path.pop()
            if node.right is not None:
                path.append(str(node.right.val))
                func(node.right, path)
                path.pop()
        
        func(root, [str(root.val)])
        return res