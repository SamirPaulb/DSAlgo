# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        i = 0
        while i < n+1 and fast:
            fast = fast.next
            i += 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        tmp = slow.next.next
        slow.next.next = None
        slow.next = tmp
        
        return dummy.next