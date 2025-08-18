# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        # while not (curr is None):
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev

        def func(head: ListNode) -> ListNode:
            if head is None:
                return None
            elif head.next is None:
                return head
            else:
                tail = head.next
                res = func(head.next)
                tail.next = head
                head.next = None
                return res
        return func(head)