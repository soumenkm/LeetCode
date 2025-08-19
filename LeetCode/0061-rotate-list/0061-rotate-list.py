# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        length = 0
        tail = None
        while not (temp is None):
            length += 1
            tail = temp
            temp = temp.next
        
        k = k % length
        if k == 0:
            return head
            
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None
        tail.next = head
        return newHead