# https://leetcode.com/problems/trim-a-binary-search-tree/

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def solve(root):
            if not root: return 
            if root.val < low:
                root = solve(root.right)
            elif root.val > high:
                root = solve(root.left)
            else:
                root.left = solve(root.left)
                root.right = solve(root.right)
            return root
        
        return solve(root)
        
        
# Time: O(N)
# Space: O(1)
