# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        hasLoop = False
        while not (fast is None or fast.next is None):
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                hasLoop = True
                break
        if hasLoop:
            slow = head
            while not (slow is fast):
                slow = slow.next
                fast = fast.next
            return fast
        else:
            return None