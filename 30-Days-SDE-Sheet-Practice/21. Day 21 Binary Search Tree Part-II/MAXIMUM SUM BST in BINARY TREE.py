# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
		
            if not root:
                return True, 0, float("inf"), float("-inf")
            
            lres, lsum, lmin, lmax = dfs(root.left)
            rres, rsum, rmin, rmax = dfs(root.right)
            
            if lres and rres and lmax < root.val < rmin:
                self.result = max(self.result, root.val+lsum+rsum)
                return True, root.val+lsum+rsum, min(root.val, lmin), max(root.val, rmax)
            else:
				# it doesn't matter which value here returns after False, 
				# since the code above "if lres and rres..." will assure that 
				# it will not run the FALSE subtree to affect the final result.
                return False, 0, 0, 0 
               
        self.result = 0
        dfs(root)
        return self.result

# Time: O(N)
# Space: O(1)