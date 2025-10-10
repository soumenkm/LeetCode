# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        inList = []
        indexRange = []
        def inorder(node: TreeNode) -> None:
            if node is None:
                return
            inorder(node.left)
            if node.val == low or node.val == high:
                indexRange.append(len(inList))
            inList.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return sum(inList[indexRange[0]: indexRange[1]+1])
