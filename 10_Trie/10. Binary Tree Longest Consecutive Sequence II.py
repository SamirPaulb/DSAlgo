# https://www.lintcode.com/problem/614
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

class Solution:
    def longest_consecutive2(self, root: TreeNode) -> int:
        def postorder(root):
            if not root: return [0, 0]  # [ic, dc]
            ic = dc = 0     # increasing count, decreasing count 
            left = postorder(root.left)
            right = postorder(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    ic = max(ic, left[0]+1)
                elif root.left.val == root.val - 1:
                    dc = max(dc, left[1]+1)
            if root.right:
                if root.right.val == root.val + 1:
                    ic = max(ic, right[0]+1)
                elif root.right.val == root.val - 1:
                    dc = max(dc, right[1]+1)
            self.res = max(self.res, ic+dc+1)
            return [ic, dc]
        
        self.res = 0
        postorder(root)
        return self.res
