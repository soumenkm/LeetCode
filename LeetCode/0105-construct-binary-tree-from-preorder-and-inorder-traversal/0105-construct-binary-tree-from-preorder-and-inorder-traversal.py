# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # FIX #3: Create a hash map for O(1) lookup of inorder indices
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Keep track of the current root index in the preorder list
        self.preorder_index = 0

        def func(ini: int, inj: int) -> Optional[TreeNode]:
            # FIX #2: Correct base case for an empty slice
            if ini > inj:
                return None

            # The current root is the next element in the preorder traversal
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1 # Move to the next root
            
            # Create the root node
            root = TreeNode(root_val)

            # Find the root's position in the current inorder slice using the map
            pos = inorder_map[root_val]

            # FIX #1: Correct recursive calls
            # Recursively build the left subtree with the left part of the inorder slice
            root.left = func(ini, pos - 1)
            # Recursively build the right subtree with the right part of the inorder slice
            root.right = func(pos + 1, inj)

            return root
        
        return func(0, len(inorder) - 1)