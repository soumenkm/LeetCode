# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colHash = {}
        def preorder(node: TreeNode, row: int, col: int) -> None:
            if node is None:
                return
            
            if col not in colHash:
                colHash.update({col: defaultdict(list)})
            
            colHash[col][row].append(node.val)
            preorder(node.left, row+1, col-1)
            preorder(node.right, row+1, col+1)
        
        preorder(root, 0, 0)
        res = []
        # print(colHash)
        for c in sorted(colHash.keys()):
            val = colHash[c]
            intRes = []
            for r in sorted(val.keys()):
                intRes.extend(sorted(val[r]))
            res.append(intRes)
        
        return res
