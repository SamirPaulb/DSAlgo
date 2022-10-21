# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return True, 0
            lbalanced, lheight = dfs(root.left)
            rbalanced, rheight = dfs(root.right)
            if not lbalanced or not rbalanced or abs(lheight - rheight) > 1:
                return False, 1 + max(lheight, rheight)
            else:
                return True, 1 + max(lheight, rheight)
        
        return dfs(root)[0]