# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder, postorder):
        inorderIndexDict = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex = len(postorder) - 1
        
        def solve(l, r):
            if l > r: return None
            
            root = TreeNode(postorder[self.rootIndex]) 
            self.rootIndex -= 1
            
            i = inorderIndexDict[root.val]
            
            # As we a approaching from end and all right side nodes of i in inorder are
            # from right sub-tree so first call solve for right then left.
            root.right = solve(i+1, r)
            root.left =  solve(l, i-1)
            
            return root
        
        return solve(0, len(inorder)-1)
    
    
# Time: O(N)
# Space: O(1)
