# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        even = head
        oddHead = even.next
        odd = oddHead
        while not (even.next is None or odd.next is None):
            even.next = odd.next
            even = odd.next
            odd.next = even.next
            odd = even.next
            
        even.next = oddHead
        return head