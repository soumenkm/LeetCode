# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # pred = None
        # def findPred(node: TreeNode, key: int) -> None:
        #     nonlocal pred
        #     if node is None:
        #         return
            
        #     if key > node.val:
        #         pred = node
        #         findPred(node.right)
        #     else:
        #         findPred(node.left)
        
        # succ = None
        # def getSucc(node: TreeNode, key: int) -> None:
        #     nonlocal succ
        #     if node is None:
        #         return
            
        #     if key < node.val:
        #         succ = node
        #         findSucc(node.left)
        #     else:
        #         findSucc(node.right)
        
        def delNode(root: TreeNode, key: int) -> TreeNode:
            if root is None:
                return None
            
            if key < root.val:
                root.left = delNode(root.left, key)
            elif key > root.val:
                root.right = delNode(root.right, key)
            else:
                if root.left is None and root.right is not None:
                    return root.right
                if root.left is not None and root.right is None:
                    return root.left
                if root.left is None and root.right is None:
                    return None
                
                pred = None
                right = root.left
                while right is not None:
                    pred = right
                    right = right.right
                
                root.val = pred.val
                root.left = delNode(root.left, pred.val)
            
            return root
        
        return delNode(root, key)

        

            