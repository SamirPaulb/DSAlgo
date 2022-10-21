class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            if not root: return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        self.maxDepth = depth(root)
        self.res = 0
        
        def solve(root, d):
            if not root: return
            if d == self.maxDepth:
                self.res += root.val
            solve(root.left, d+1)
            solve(root.right, d+1)
        
        solve(root, 1)
        return self.res