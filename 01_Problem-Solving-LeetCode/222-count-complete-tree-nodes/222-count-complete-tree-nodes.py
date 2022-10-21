class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)
        if lh == rh:
            return 2 ** lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    
    def leftHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
    
    def rightHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height