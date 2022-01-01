# https://www.youtube.com/watch?v=zmPj_Ee3B8c&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=47
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root):
            # Base Case : Tree is empty
            if not root: return 0
            
            l = solve(root.left)  # diameter of left subtree
            r = solve(root.right) # diameter of right subtree
            
            temp = 1 + max(l, r)
            # update the answer, because diameter of a tree is nothing but maximum value of (left_height + right_height + 1) for each node
            ans = max(temp, 1 + l + r)
            self.res = max(self.res, ans)  # if current path is longer than previous then update res
            
            return temp  # returning temp insted of res; longest path may not include current node or left or right subtree
        
        solve(root)
        return self.res

    
# Time Complexity: O(n) 
# Space Complexity: O(1)

'''
Input :     1
          /   \
        2      3
      /  \
    4     5

Output : 4


Input :     1
          /   \
        2      3
      /  \      \
    4     5      6

Output : 5

'''