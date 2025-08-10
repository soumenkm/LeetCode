# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode) -> None:
        self.leftStack = deque()
        self.rightStack = deque()
        self.insertLeft(root)
        self.insertRight(root)
    
    def insertLeft(self, root: TreeNode) -> None:
        while root is not None:
            self.leftStack.append(root)
            root = root.left
    
    def insertRight(self, root: TreeNode) -> None:
        while root is not None:
            self.rightStack.append(root)
            root = root.right
    
    def next(self) -> int:
        if self.hasNext():
            node = self.leftStack.pop()
            self.insertLeft(node.right)
            return node.val
        else:
            return None
    
    def before(self) -> int:
        if self.hasBefore():
            node = self.rightStack.pop()
            self.insertRight(node.left)
            return node.val
        else:
            return None
    
    def hasNext(self) -> bool:
        return len(self.leftStack) != 0
    
    def hasBefore(self) -> bool:
        return len(self.rightStack) != 0

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        itr = BSTIterator(root)
        i = itr.next()
        j = itr.before()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = itr.next()
            elif i + j > k:
                j = itr.before()
        return False