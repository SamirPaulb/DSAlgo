class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def binarySearch(l, r):
            if l > r: return None
            mid = (l+r) // 2
            root = TreeNode(arr[mid])
            root.left = binarySearch(l, mid-1)
            root.right = binarySearch(mid+1, r)
            return root
        
        return binarySearch(0, len(arr)-1)