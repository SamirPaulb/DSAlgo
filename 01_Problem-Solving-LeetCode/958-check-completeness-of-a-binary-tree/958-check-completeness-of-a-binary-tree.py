# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        have_null_between = False
        
        while q:
            node = q.pop(0)
            if not node:
                have_null_between = True
                continue
            if have_null_between == True: return False
            q.append(node.left)
            q.append(node.right)
        
        return True