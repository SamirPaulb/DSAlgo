class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            a = lists.pop()
            b = lists.pop()
            
            c = self.merge2SortedList(a, b)
            
            lists.append(c)
        
        return lists[0] if lists else None
        
    
    def merge2SortedList(self, l1, l2):
        if not l1 or not l2: return l2 or l1
        
        if l1.val <= l2.val: a = l1; b = l2
        else: a = l2; b = l1
        
        res = a
        
        while a or b:
            if not b: a.next = b; break
            if not a.next: a.next = b; break
            
            if a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
            
            a = a.next
        
        return res
    
    
# Time: O(k * len(max(lists)))
# Space: O(len(max(lists)))