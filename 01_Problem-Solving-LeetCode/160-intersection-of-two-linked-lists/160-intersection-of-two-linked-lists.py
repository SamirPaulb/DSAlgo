# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        loopCount = 0
        
        while True:   
            if a == b: return a
            
            a = a.next
            b = b.next
            
            if not a: a = headB; loopCount += 1
            if not b: b = headA
            
            if loopCount > 1: return None
                