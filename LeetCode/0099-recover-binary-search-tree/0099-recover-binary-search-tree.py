# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # def printRes(root, prev, curr, res):
        #     r = root.val if root else None
        #     p = prev.val if prev else None
        #     c = curr.val if curr else None
        #     if len(res) == 1:
        #         re = res[0][0].val, res[0][1].val
        #     else:
        #         re = None
        #     print(f"root: {r}, prev: {p}, curr: {c}, res: {re}")


        prev = TreeNode(-math.inf)
        curr = None
        res = []
        def inorder(root: TreeNode) -> None:
            nonlocal prev
            nonlocal curr
            # printRes(root, prev, curr, res)
            if root is None:
                return
            
            inorder(root.left)
            curr = root
            if curr.val < prev.val:
                res.append([prev, curr])
            prev = curr
            inorder(root.right)
        
        inorder(root)
        if len(res) == 1:
            prev, curr = res[0]
        elif len(res) == 2:
            prev, curr = res[0][0], res[1][1]
        else:
            raise ValueError("Something is wrong!")

        # print(prev.val, curr.val)
        prev.val, curr.val = curr.val, prev.val
        # print(prev.val, curr.val)
