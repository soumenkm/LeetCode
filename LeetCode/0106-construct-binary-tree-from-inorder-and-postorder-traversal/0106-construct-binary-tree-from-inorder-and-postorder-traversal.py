# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}
        n = len(postorder)
        postIndex = n - 1
        def func(inStart: int, inEnd: int) -> TreeNode:
            nonlocal postIndex
            # print(inStart, inEnd)
            if inStart > inEnd:
                return None

            rootVal = postorder[postIndex]
            pos = inorderMap[rootVal]
            postIndex = postIndex - 1
            right = func(pos+1, inEnd)
            left = func(inStart, pos-1)
            root = TreeNode(rootVal, left, right)
            return root

        root = func(0, n-1)
        return root