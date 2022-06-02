# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Solution:
    def buildTree(self, preorder, inorder):
        inorderIndexDict = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex = 0
        
        def solve(l, r):
            if l > r: return None
            
            root = TreeNode(preorder[self.rootIndex])
            self.rootIndex += 1
            
            i = inorderIndexDict[root.val]
            
            # As we a approaching from begining and all left side nodes of i in inorder are
            # from left sub-tree so first call solve for left then right.
            root.left = solve(l, i-1)
            root.right = solve(i+1, r)
            
            return root
        
        return solve(0, len(inorder)-1)
    
    
# Time: O(N)
# Space: O(1)

