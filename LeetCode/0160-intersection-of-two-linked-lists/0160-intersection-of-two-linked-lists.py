# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def printList(self, node: ListNode, name: str):
        print(f"{name}: ", end="")
        while node is not None:
            print(f"{node.val} --> ", end="")
            node = node.next
        print("NULL")

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1 = headA
        t2 = headB
        while not (t1 is t2):
            # self.printList(t1, "t1")
            # self.printList(t2, "t2")
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA

        return t1
        
        