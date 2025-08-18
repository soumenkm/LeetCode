# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMiddle(head: ListNode) -> ListNode:
            slow = head
            fast = head
            prev = None
            while not (fast is None or fast.next is None):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            return prev
        
        if head.next is None:
            return None

        middle = findMiddle(head)
        delNode = middle.next
        if delNode.next is None:
            middle.next = None
        else:
            middle.next = delNode.next
        return head