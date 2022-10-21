# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        isCycle = False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                isCycle = True
                break
        
        if isCycle == False: return None
        
        while True:
            if head == slow: return slow
            head = head.next
            slow = slow.next
            
        