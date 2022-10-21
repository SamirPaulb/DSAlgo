# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: 
                return True, 0, float("inf"), float("-inf")
            lRes, lSum, lMin, lMax = dfs(root.left)
            rRes, rSum, rMin, rMax = dfs(root.right)
            
            if lRes and rRes and lMax < root.val < rMin:
                self.res = max(self.res, lSum + root.val + rSum)
                return True, lSum + root.val + rSum, min(lMin, root.val), max(rMax, root.val)
            
            else:
                return False, 0, 0, 0
        
        self.res = 0
        dfs(root)
        return self.res