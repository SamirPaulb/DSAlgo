# https://leetcode.com/problems/merge-two-sorted-lists/
''' 
Take 2 pointers on 2 lists. compare values of pointers.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	
        if not list1 or not list2: return list2 or list1
        
        if list1.val <= list2.val: a = list1; b = list2
        else: a = list2; b = list1
            
        res = a
        
        while a:
            if not a.next: a.next = b; return res
            elif not b: return res
            elif a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
            a = a.next
        
        return res

# Time: O(n + m)  # We are still traversing both lists entirely in the worst-case scenario
# Space: O(1)     # We are using the same lists just changing links to create our desired list. So no extra space is used. 