# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        pre = []
        def preorder(node: TreeNode) -> None:
            if node is None:
                pre.append("N")
                return
            
            pre.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        preStr = "_".join(pre)
        return preStr


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        pre = data.split("_")
        n = len(pre)
        
        Q = deque(pre)
        def func() -> TreeNode:
            rootVal = Q.popleft()
            if rootVal == "N":
                return None
            
            left = func()
            right = func()
            root = TreeNode(int(rootVal), left, right)
            return root
        
        return func()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))