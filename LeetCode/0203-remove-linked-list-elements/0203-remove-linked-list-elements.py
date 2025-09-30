# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        ptr = head
        while ptr is not None:
            while ptr is not None and ptr.val == val:
                ptr = ptr.next
            temp.next = ptr
            temp = ptr
            if ptr is not None:
                ptr = ptr.next
        return dummy.next
