"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp = head
        while not (temp is None):
            copyNode = Node(temp.val)
            nextNode = temp.next
            temp.next = copyNode
            copyNode.next = nextNode
            temp = nextNode
        
        orig = head
        copy = head.next
        while not (copy is None and orig is None):
            randNode = orig.random
            copy.random = randNode.next if randNode else None
            orig = copy.next
            copy = orig.next if orig else None
        
        orig = head
        copy = head.next
        dummy = Node(-1)
        temp = dummy
        while not (orig is None and copy is None):
            orig.next = copy.next
            orig = copy.next
            copy.next = orig.next if orig else None
            temp.next = copy
            temp = copy
            copy = orig.next if orig else None
        
        return dummy.next