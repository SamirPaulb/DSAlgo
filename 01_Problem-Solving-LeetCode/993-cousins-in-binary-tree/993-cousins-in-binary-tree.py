class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.px = root
        self.py = root
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
        
        def solve(r, p, d):  #(current root, parent, depth)
            if not r: return
            if r.val == self.x:
                self.px = p.val
                self.dx = d
            if r.val == self.y:
                self.py = p.val
                self.dy = d
            solve(r.left, r, d+1)
            solve(r.right, r, d+1)
        
        solve(root, root, 0)
        
        return self.px != self.py and self.dx == self.dy