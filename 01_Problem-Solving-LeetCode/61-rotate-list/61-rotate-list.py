# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        a = head
        
        length = 0
        while a:
            length += 1
            a = a.next
        
        k = k % length
        
        if k == 0: return head
        
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next
        slow.next = None
        
        fast.next = dummy.next
        dummy.next = tmp
        
        return dummy.next