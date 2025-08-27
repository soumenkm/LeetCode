# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        PQ = []
        count = 0
        for head in lists:
            if head is not None:
                heapq.heappush(PQ, (head.val, count, head))
                count += 1
        
        dummy = ListNode(-math.inf)
        temp = dummy
        while not (len(PQ) == 0):
            minVal, _, minNode = heapq.heappop(PQ)
            temp.next = minNode
            temp = temp.next
            if minNode.next is not None:
                nextNode = minNode.next
                heapq.heappush(PQ, (nextNode.val, count, nextNode))
                count += 1
        
        return dummy.next

