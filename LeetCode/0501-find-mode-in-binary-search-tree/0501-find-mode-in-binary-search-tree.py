# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashMap = defaultdict(int)
        def func(node) -> None:
            if node is None:
                return

            hashMap[node.val] += 1
            func(node.left)
            func(node.right)
        
        func(root)
        inverseMap = defaultdict(list)
        for key, val in hashMap.items():
            inverseMap[val].append(key)
        
        # print(inverseMap)
        # print(hashMap)
        maxKey = max(inverseMap.keys())
        return inverseMap[maxKey]
