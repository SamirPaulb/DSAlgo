# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(mini, root, maxi):
            if not root: return True
                        
            return (mini < root.val < maxi and 
                   check(mini, root.left, root.val) and
                   check(root.val, root.right, maxi))
        
        return check(-2**31-1, root, 2**31)

