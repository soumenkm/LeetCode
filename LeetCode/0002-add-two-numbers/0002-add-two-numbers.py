# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(math.inf, None)
        temp = dummy
        carry = 0
        while not (temp1 is None and temp2 is None):
            if temp1 is None and temp2 is not None:
                carry, addVal = divmod(temp2.val + carry, 10)
                temp2 = temp2.next
            elif temp2 is None and temp1 is not None:
                carry, addVal = divmod(temp1.val + carry, 10)
                temp1 = temp1.next
            else:
                carry, addVal = divmod(temp1.val + temp2.val + carry, 10)
                temp1 = temp1.next
                temp2 = temp2.next

            resNode = ListNode(addVal, None)
            temp.next = resNode
            temp = temp.next
        
        if carry > 0:
            resNode = ListNode(carry, None)
            temp.next = resNode
        
        return dummy.next