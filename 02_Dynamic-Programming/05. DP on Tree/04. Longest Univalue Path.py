# https://leetcode.com/problems/longest-univalue-path/
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # same as diameter of binary tree problem
        self.res = 0
        def solve(root):
            if not root: return 0
            lMax = solve(root.left)
            rMax = solve(root.right)
            
            if root.left:
                if root.val == root.left.val: lMax += 1
                else: lMax = 0
            if root.right:
                if root.val == root.right.val: rMax += 1
                else: rMax = 0
            
            self.res = max(self.res, lMax + rMax)
            return max(lMax, rMax)
        
        solve(root)
        return self.res