class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 or not root2: return root2 or root1
        
        root1.val += root2.val
        
        if not root1.left: 
            root1.left = root2.left
        else:
            self.mergeTrees(root1.left, root2.left)
            
        if not root1.right: 
            root1.right = root2.right
        else:
            self.mergeTrees(root1.right, root2.right)
            
        return root1