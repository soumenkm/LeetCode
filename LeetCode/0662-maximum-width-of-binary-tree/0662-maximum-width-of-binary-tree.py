# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Q = deque()
        Q.append((root, 0))
        res = []
        while len(Q) != 0:
            n = len(Q)
            intRes = []
            for i in range(n):
                node, j = Q.popleft()
                if node is not None:
                    intRes.append(j)
                
                if node.left is not None:
                    Q.append((node.left, 2*j+1))
                
                if node.right is not None:
                    Q.append((node.right, 2*j+2))
            
            res.append(intRes[-1] - intRes[0] + 1)

        return max(res)