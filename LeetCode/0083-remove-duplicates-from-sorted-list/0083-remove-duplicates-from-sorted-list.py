# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp is not None:
            front = temp.next
            while front is not None and front.val == temp.val:
                front = front.next
            temp.next = front
            temp = front
        return head