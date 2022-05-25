# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        loopCount = 0   # if no intersection
        
        while True:   
            if a == b: return a
            
            a = a.next
            b = b.next
            
            if not a: a = headB; loopCount += 1
            if not b: b = headA
            
            if loopCount > 1: return None

# Time: O(n + m)
# Space: O(1)