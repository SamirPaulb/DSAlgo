class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 
        
        def solve(root):
            if not root: return True
            
            l = solve(root.left)
            r = solve(root.right)
            
            if l: root.left = None
            if r: root.right = None
            if not root.left and not root.right and root.val == 0: return True 
            return False
        
        solve(root)
        if not root.left and not root.right and root.val == 0: return None
        return root