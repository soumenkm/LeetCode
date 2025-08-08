# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(nodeLeft: TreeNode, nodeRight: TreeNode) -> bool:
            if nodeLeft is None and nodeRight is None:
                return True
            if nodeLeft is None or nodeRight is None:
                return False
            # print(nodeLeft.val, nodeRight.val)
            res1 = isMirror(nodeLeft.left, nodeRight.right)
            res2 = isMirror(nodeLeft.right, nodeRight.left)
            if res1 and res2 and nodeLeft.val == nodeRight.val:
                return True
            else:
                return False
        
        res = isMirror(root.left, root.right)
        return res