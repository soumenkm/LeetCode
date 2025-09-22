# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode(val=float("inf"))
        temp = dummy

        while not (head1 is None or head2 is None):
            if head1.val < head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        
        if head1 is None:
            temp.next = head2
        elif head2 is None:
            temp.next = head1
        
        return dummy.next
