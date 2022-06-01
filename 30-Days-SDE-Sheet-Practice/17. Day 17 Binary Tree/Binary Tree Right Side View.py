# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        
        q = collections.deque()
        q.append(root)
        
        while q:
            res.append(q[-1].val)  # the top element of q is the right-most
            n = len(q)             # popping all elements of a level at a time
            for i in range(n):     # first n nodes of q are nodes of current level
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res
    
# Instead of using array as a queue we should use collections.deque()
# as pop() 0'th element from deque is of O(1) time.

# Time: O(N)
# Space: O(N)
