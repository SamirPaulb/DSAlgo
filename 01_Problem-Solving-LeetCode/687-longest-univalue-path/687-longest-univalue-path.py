class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root):
            if not root: return 0
            
            leftMax = solve(root.left)
            rightMax = solve(root.right)
            
            if root.left:
                if root.val == root.left.val: leftMax += 1
                else: leftMax = 0
                    
            if root.right:
                if root.val == root.right.val: rightMax += 1
                else: rightMax = 0
            
            self.res = max(self.res, leftMax + rightMax)
            return max(leftMax, rightMax)
        
        solve(root)
        return self.res