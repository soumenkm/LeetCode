'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
from copy import deepcopy
import math

class Solution:
    def findPreSuc(self, root, key):
        #
        # temp = root
        # pred = None
        # succ = None
        
        # while root is not None:
        #     if key < root.data:
        #         succ = root
        #         root = root.left
        #     elif key > root.data:
        #         pred = root
        #         root = root.right
        #     else:
        #         temp1 = root.left
        #         temp2 = root.right
                
        #         while temp1 is not None:
        #             pred = temp1
        #             temp1 = temp1.right
                
        #         while temp2 is not None:
        #             succ = temp2
        #             temp2 = temp2.left
                
        #         break
        
        # return pred, succ
        
        pred = None
        def findPred(root, key):
            nonlocal pred
            # print(root.data if root else None, pred.data if pred else None)
            if root is None:
                return
            if key > root.data:
                pred = root
                findPred(root.right, key)
            else:
                findPred(root.left, key)
        
        succ = None
        def findSucc(root, key):
            nonlocal succ
            # print(root.data if root else None, succ.data if succ else None)
            if root is None:
                return
            if key < root.data:
                succ = root
                findSucc(root.left, key)
            else:
                findSucc(root.right, key)
        
        findPred(root, key)
        findSucc(root, key)
        return pred, succ
        
                    
                    