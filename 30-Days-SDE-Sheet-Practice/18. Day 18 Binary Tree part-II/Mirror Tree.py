# https://practice.geeksforgeeks.org/problems/mirror-tree/1#

class Solution:
    def mirror(self,root):
        
        def solve(root):
            if not root: return
            solve(root.left)
            solve(root.right)
            l = root.left
            r = root.right
            root.left = r
            root.right = l
            
        solve(root)
        return root

# Time: O(N)
# Space: O(1)