# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque()
        Q.append((root, 0))
        res = defaultdict(list)
        while len(Q) != 0:
            node, level = Q.popleft()
            res[level].append(node.val)
            if node.left is not None:
                Q.append((node.left, level+1))
            if node.right is not None:
                Q.append((node.right, level+1))
        
        finalRes = []
        for k in sorted(res.keys()):
            finalRes.append(res[k])
        
        return finalRes

