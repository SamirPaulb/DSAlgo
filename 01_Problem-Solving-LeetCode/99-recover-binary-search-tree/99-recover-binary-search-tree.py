class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        self.first = None
        self.second = None
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorder(root.right)
            
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root