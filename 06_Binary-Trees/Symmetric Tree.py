# https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(l, r):
            if not l and not r: 
                return True
            if not l or not r:
                return False
            
            return l.val == r.val and solve(l.left, r.right) and solve(l.right, r.left)
        
        return solve(root.left, root.right)
    
# Time: O(N)
# Space: O(1)