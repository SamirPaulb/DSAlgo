# https://leetcode.com/problems/house-robber-iii/

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return [0, 0]
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            
            withRoot = root.val + leftPair[1] + rightPair[1]
            withOutRoot = max(leftPair) + max(rightPair)
            
            return [withRoot, withOutRoot]
        
        return max(dfs(root))
