# https://practice.geeksforgeeks.org/problems/largest-bst/1#

class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        def solve(root):
            if not root: 
                return True, float('inf'), float('-inf'), 0
            if not root.left and not root.right:
                return True, root.data, root.data, 1
            lBST, lMin, lMax, lRes = solve(root.left)
            rBST, rMin, rMax, rRes = solve(root.right)
            if lBST and rBST and lMax < root.data < rMin:
                return True, min(lMin, root.data), max(rMax, root.data), 1 + lRes + rRes
            else:
                return False, 0, 0, max(lRes, rRes)
        
        return solve(root)[3]
      
# Time: O(N)
# Auxiliary Space: O(N)
