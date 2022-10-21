class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2: return list2 or list1
        
        if list1.val <= list2.val: a = list1; b = list2
        else: a = list2; b = list1
        
        res = a
        
        while a or b:
            if not b: break
            if not a.next: a.next = b; break
            if a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
            a = a.next
        
        return res