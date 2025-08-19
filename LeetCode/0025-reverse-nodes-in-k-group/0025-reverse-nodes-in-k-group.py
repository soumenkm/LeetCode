# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head: ListNode) -> ListNode:
            curr = head
            prev = None
            while not (curr is None):
                front = curr.next
                curr.next = prev
                prev = curr
                curr = front
            return prev
        
        dummy = ListNode(math.inf, None)
        ptr = dummy

        temp = head
        kHead = head
        while True:
            for i in range(k-1):
                if temp is None:
                    break
                temp = temp.next
            if temp is not None:
                kTail = temp
                temp = temp.next
                kTail.next = None
                nHead = rev(kHead)
                ptr.next = nHead
                ptr = kHead
                kHead = temp
            else:
                ptr.next = kHead
                break
        return dummy.next
            