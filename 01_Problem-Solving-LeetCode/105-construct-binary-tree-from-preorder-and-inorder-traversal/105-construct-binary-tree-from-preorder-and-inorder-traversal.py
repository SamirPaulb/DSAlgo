# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorderIndx = {inorder[i] : i for i in range(n)}
        self.pi = 0
        
        def solve(l, r):
            if l > r: return None
            v = preorder[self.pi]
            self.pi += 1
            root = TreeNode(v)
            i = inorderIndx[v]
            root.left = solve(l, i-1)
            root.right = solve(i+1, r)
            return root
        
        return solve(0, n-1)