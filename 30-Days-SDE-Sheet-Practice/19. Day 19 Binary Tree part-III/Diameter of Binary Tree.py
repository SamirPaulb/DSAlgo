# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root):
            if not root: return 0
            
            l = solve(root.left)
            r = solve(root.right)
            
            tmp = 1 + max(l, r)
            self.res = max(self.res, 1 + l + r)
            
            return tmp
        
        solve(root)
        return self.res - 1


