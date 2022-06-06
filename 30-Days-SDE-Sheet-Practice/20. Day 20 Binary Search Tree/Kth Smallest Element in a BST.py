# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = root.val
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.k -= 1
            if self.k == 0: self.res = root.val
            inorder(root.right)
        
        inorder(root)
        return self.res

# Time: O(N)
# Space: O(1)