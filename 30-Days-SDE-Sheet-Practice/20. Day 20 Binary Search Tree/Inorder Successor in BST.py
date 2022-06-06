# https://www.lintcode.com/problem/448/description
# https://leetcode.com/problems/inorder-successor-in-bst/   (Premium)
class Solution:
    def inorderSuccessor(self, root, p):
        res = None
        while root:
            if root.val > p.val:
                res = root  # current root is greater so it can be a successor. 
                root = root.left  # check if lesser root exit or not
            else:
                root = root.right  # current root is lesser than p try for greater roots

        return res

# Time: O(log(N))
# Space: O(1)

