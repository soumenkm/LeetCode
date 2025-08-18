# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        fast = head
        for i in range(n):
            fast = fast.next
        
        if fast is None:
            head = head.next
            return head

        slow = head
        while not (fast.next is None):
            fast = fast.next
            slow = slow.next
        
        delNode = slow.next
        if n == 1:
            slow.next = None
        else:
            slow.next = delNode.next
        return head
