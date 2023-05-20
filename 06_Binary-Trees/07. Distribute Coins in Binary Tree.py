# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# https://youtu.be/MvLEIQv4E6s

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root):
            if not root: return 0
            l = solve(root.left)
            r = solve(root.right)
            self.res += abs(l) + abs(r)
            return l + r + root.val - 1
        
        solve(root)
        return self.res
