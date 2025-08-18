# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while not (fast is None or fast.next is None):
            fast = fast.next.next
            slow = slow.next
        
        def rev(head: ListNode) -> ListNode:
            back = None
            curr = head
            while not (curr is None):
                front = curr.next
                curr.next = back
                back = curr
                curr = front
            return back
        
        end = rev(slow)
        start = head
        while not (end is None):
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True