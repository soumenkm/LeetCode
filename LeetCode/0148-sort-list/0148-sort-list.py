# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, head: ListNode) -> None:
        while not (head is None):
            print(head.val, " --> ")
            head = head.next
        print("NULL")

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left: ListNode, right: ListNode) -> ListNode:
            if left is None:
                return right
            if right is None:
                return left

            dummy = ListNode(math.inf, None)
            temp = dummy
            while not (left is None or right is None):
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next  
            
            if left is None:
                temp.next = right
            if right is None:
                temp.next = left
            return dummy.next
        
        def findMiddle(head: ListNode) -> ListNode:
            fast = head
            slow = head
            prev = None
            while not (fast is None or fast.next is None):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            if fast is None:
                return prev
            if fast.next is None:
                return slow

        def mergeSort(head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            
            middle = findMiddle(head)
            left = head
            right = middle.next
            middle.next = None
            leftHead = mergeSort(left)
            rightHead = mergeSort(right)
            sortedHead = merge(leftHead, rightHead)
            return sortedHead
        
        return mergeSort(head)