# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def solve(inorder, postorder):
            if not postorder: return None
            root = TreeNode(postorder.pop())
            i = inorder.index(root.val)
            root.left = solve(inorder[:i], postorder[:i])
            root.right = solve(inorder[i+1:], postorder[i:])
            return root
        
        return solve(inorder, postorder)