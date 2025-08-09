# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def func(src: TreeNode, dest: TreeNode, path: List[int]) -> bool:
        #     if src is None:
        #         return False

        #     path.append(src)
        #     if dest.val == src.val:
        #         return True
            
        #     isPresLeft = func(src.left, dest, path)
        #     if isPresLeft:
        #         return True
            
        #     isPresRight = func(src.right, dest, path)
        #     if isPresRight:
        #         return True
            
        #     path.pop()
        #     return False
        
        # pPath = []
        # qPath = []
        # func(root, p, pPath)
        # func(root, q, qPath)

        # n = min(len(pPath), len(qPath))
        # res = None
        # for i in range(n):
        #     if pPath[i].val == qPath[i].val:
        #         res = pPath[i]
        #     else:
        #         break
        
        # return res


        def func(node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if node is p:
                return p
            if node is q:
                return q
            
            left = func(node.left)
            right = func(node.right)
            if left is None and right is None:
                return None
            if left is not None and right is None:
                return left
            if right is not None and left is None:
                return right
            if right is not None and left is not None:
                return node
        
        return func(root)